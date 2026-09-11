"""Single-query scaled dot-product attention for small teaching inputs."""
import math


def vector(values):
    if not isinstance(values, (list, tuple)) or not 1 <= len(values) <= 64:
        raise ValueError("use a nonempty vector with at most 64 entries")
    if any(type(x) not in (int, float) or not math.isfinite(x) or abs(x) > 10**6 for x in values):
        raise ValueError("entries must be finite numbers with magnitude <= 10**6")
    return list(values)


def softmax(scores):
    scores = vector(scores)
    maximum = max(scores)
    exponentials = [math.exp(x - maximum) for x in scores]
    total = sum(exponentials)
    return [x / total for x in exponentials]


def attention(query, keys, values):
    query = vector(query)
    if not isinstance(keys, (list, tuple)) or not isinstance(values, (list, tuple)):
        raise ValueError("keys and values must be matrices")
    if not 1 <= len(keys) <= 64 or len(keys) != len(values):
        raise ValueError("use one to 64 paired keys and values")
    keys = [vector(k) for k in keys]
    values = [vector(v) for v in values]
    if any(len(k) != len(query) for k in keys):
        raise ValueError("query and key dimensions must match")
    if any(len(v) != len(values[0]) for v in values):
        raise ValueError("value rows must have equal lengths")
    scores = [sum(a*b for a, b in zip(query, k)) / math.sqrt(len(query)) for k in keys]
    # Softmax subtracts its maximum internally and enforces the teaching range.
    weights = softmax(scores)
    output = [sum(w*v[j] for w, v in zip(weights, values)) for j in range(len(values[0]))]
    return {"scores": scores, "weights": weights, "output": output}


if __name__ == "__main__":
    for query in ([1, 0], [0, 1], [0, 0]):
        result = attention(query, [[1, 0], [0, 1]], [[10, 0], [0, 20]])
        print(f"query={query}")
        for label, values in result.items():
            print(f"{label}={[round(x, 6) for x in values]}")
