import math
import unittest
from demo.attention import attention, softmax
from demo.identity_checker import normalize, check_identity


class AttentionTests(unittest.TestCase):
    def test_known_formula(self):
        result = attention([1, 0], [[1, 0], [0, 1]], [[10, 0], [0, 20]])
        weight = math.exp(1 / math.sqrt(2)) / (1 + math.exp(1 / math.sqrt(2)))
        self.assertAlmostEqual(result['weights'][0], weight)
        self.assertAlmostEqual(result['output'][0], 10*weight)
        self.assertAlmostEqual(result['output'][1], 20*(1-weight))

    def test_uniform_single_and_shift_invariance(self):
        self.assertEqual(softmax([0, 0]), [0.5, 0.5])
        self.assertEqual(attention([1], [[2]], [[3, 4]])['output'], [3, 4])
        for a, b in zip(softmax([1, 2]), softmax([10001, 10002])):
            self.assertAlmostEqual(a, b)

    def test_pair_permutation(self):
        original = attention([1, 0], [[1, 0], [0, 1]], [[10], [20]])
        reversed_pairs = attention([1, 0], [[0, 1], [1, 0]], [[20], [10]])
        self.assertEqual(original['output'], reversed_pairs['output'])

    def test_invalid_inputs(self):
        for scores in ([], [float('inf')], [float('nan')], [True], ['1'], [10**7]):
            with self.assertRaises(ValueError):
                softmax(scores)
        for q, k, v in (([], [[1]], [[1]]), ([1], [], []), ([1], [[1, 2]], [[1]]), ([1], [[1]], []), ([1], [[1], [2]], [[1], [1, 2]])):
            with self.assertRaises(ValueError):
                attention(q, k, v)


class IdentityTests(unittest.TestCase):
    def test_normal_form_and_identities(self):
        self.assertEqual(normalize('(x+1)**2'), {2: 1, 1: 2, 0: 1})
        for left, right in (('(x+1)**2', 'x**2+2*x+1'), ('(x-1)*(x+1)', 'x**2-1'), ('x-x', '0'), ('x**0', '1'), ('-x+x', '0')):
            self.assertTrue(check_identity(left, right)['identity'])

    def test_wrong_claim_and_sample_trap(self):
        self.assertFalse(check_identity('(x+1)**2', 'x**2+1')['identity'])
        trap = check_identity('x*(x-1)*(x+1)*(x-2)*(x+2)*(x-3)*(x+3)', '0')
        self.assertFalse(trap['identity'])
        self.assertIsNone(trap['counterexample'])
        self.assertEqual(trap['difference'][7], 1)

    def test_reject_outside_language(self):
        for text in ('x/x', 'x**-1', 'x**7', 'y', 'True', '2.5', 'abs(x)', 'x^2', '__import__("os")', 'x[0]', '', 'x+' , 'x'*257, '((x**6)**6)'):
            with self.assertRaises(ValueError, msg=text):
                normalize(text)


if __name__ == '__main__':
    unittest.main()
