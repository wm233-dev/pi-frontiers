import unittest
from itertools import combinations
from math import prod
from demo.primes import euclid_example, is_prime, prime_factors


class PrimeDemoTests(unittest.TestCase):
    def test_known_primes_and_composites(self):
        for n in (2, 3, 31, 59, 509):
            self.assertTrue(is_prime(n))
        for n in (-5, 0, 1, 4, 49, 30031):
            self.assertFalse(is_prime(n))

    def test_counterexample(self):
        self.assertEqual(euclid_example([2, 3, 5, 7, 11, 13]), (30031, [59, 509]))

    def test_repeated_factor_and_smaller_new_prime(self):
        self.assertEqual(euclid_example([3, 5]), (16, [2, 2, 2, 2]))
        self.assertEqual(prime_factors(49), [7, 7])

    def test_all_nonempty_subsets_of_six_primes(self):
        for size in range(1, 7):
            for values in combinations([2, 3, 5, 7, 11, 13], size):
                number, factors = euclid_example(list(values))
                self.assertEqual(number, prod(values) + 1)
                self.assertEqual(prod(factors), number)
                self.assertTrue(set(factors).isdisjoint(values))
                for q in factors:
                    # Independent definition check over the full divisor range.
                    self.assertGreater(q, 1)
                    self.assertFalse(any(q % d == 0 for d in range(2, q)))

    def test_invalid_teaching_inputs(self):
        for values in ([], [2, 2], [4], [1], [37], [True], [2.0], list(range(9))):
            with self.assertRaises(ValueError):
                euclid_example(values)
        for value in (1, 0, -1, 10**12 + 1):
            with self.assertRaises(ValueError):
                prime_factors(value)
        for value in (True, 2.0, "2"):
            with self.assertRaises(TypeError):
                prime_factors(value)
            with self.assertRaises(TypeError):
                is_prime(value)


if __name__ == "__main__":
    unittest.main()
