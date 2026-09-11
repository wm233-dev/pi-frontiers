"""Exact normalization of bounded univariate integer polynomials.

Not Lean, not a general proof assistant. No eval, model, network or dependencies.
Input: x, small integer constants, +, -, *, ** (literal exponents 0..6).
"""
import ast


def clean(poly):
    result = {d: c for d, c in poly.items() if c}
    if any(d > 32 or abs(c) > 10**100 for d, c in result.items()):
        raise ValueError("polynomial exceeds teaching limits")
    return result


def add(a, b, sign=1):
    result = a.copy()
    for degree, coefficient in b.items():
        result[degree] = result.get(degree, 0) + sign*coefficient
    return clean(result)


def multiply(a, b):
    result = {}
    for da, ca in a.items():
        for db, cb in b.items():
            result[da+db] = result.get(da+db, 0) + ca*cb
    return clean(result)


def normalize(expression):
    if not isinstance(expression, str) or not 1 <= len(expression) <= 256:
        raise ValueError("expression must contain 1..256 characters")
    try:
        tree = ast.parse(expression.strip(), mode="eval")
    except (SyntaxError, RecursionError) as error:
        raise ValueError("invalid expression") from error
    if len(list(ast.walk(tree))) > 128:
        raise ValueError("expression is too complex")

    def visit(node):
        if isinstance(node, ast.Constant) and type(node.value) is int and abs(node.value) <= 1000:
            return clean({0: node.value})
        if isinstance(node, ast.Name) and node.id == "x":
            return {1: 1}
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            return {d: (-c if isinstance(node.op, ast.USub) else c) for d, c in visit(node.operand).items()}
        if isinstance(node, ast.BinOp):
            if isinstance(node.op, ast.Pow):
                if not isinstance(node.right, ast.Constant) or type(node.right.value) is not int or not 0 <= node.right.value <= 6:
                    raise ValueError("power must be a literal integer from 0 to 6")
                base, result = visit(node.left), {0: 1}
                for _ in range(node.right.value):
                    result = multiply(result, base)
                return result
            if isinstance(node.op, (ast.Add, ast.Sub, ast.Mult)):
                left, right = visit(node.left), visit(node.right)
                if isinstance(node.op, ast.Mult):
                    return multiply(left, right)
                return add(left, right, -1 if isinstance(node.op, ast.Sub) else 1)
        raise ValueError("unsupported syntax; only integer polynomials in x are accepted")

    return visit(tree.body)


def evaluate(poly, x):
    return sum(c*x**d for d, c in poly.items())


def check_identity(left, right):
    a, b = normalize(left), normalize(right)
    difference = add(a, b, -1)
    witness = next((x for x in range(-3, 4) if evaluate(difference, x) != 0), None)
    return {"identity": not difference, "difference": difference, "counterexample": witness}


if __name__ == "__main__":
    examples = [
        ("(x+1)**2", "x**2+2*x+1"),
        ("(x+1)**2", "x**2+1"),
        ("x*(x-1)*(x+1)", "0"),
        ("x*(x-1)*(x+1)*(x-2)*(x+2)*(x-3)*(x+3)", "0"),
    ]
    for left, right in examples:
        print(f"{left} == {right}")
        print(check_identity(left, right))
