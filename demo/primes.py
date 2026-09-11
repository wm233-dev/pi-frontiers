"""Finite examples for Euclid's argument, not a proof of infinitude.

Small teaching inputs only: at most eight distinct primes, each <= 31.
Python 3.10+, standard library only.
"""
from math import isqrt, prod


def is_prime(n: int) -> bool:
    if type(n) is not int:
        raise TypeError("n must be an integer, not a bool")
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def prime_factors(n: int) -> list[int]:
    if type(n) is not int:
        raise TypeError("n must be an integer, not a bool")
    if not 2 <= n <= 10**12:
        raise ValueError("use a small integer from 2 to 10**12")
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factors.append(n)
    return factors


def euclid_example(primes: list[int]) -> tuple[int, list[int]]:
    if not 1 <= len(primes) <= 8:
        raise ValueError("supply one to eight primes")
    if any(type(p) is not int or not 2 <= p <= 31 for p in primes):
        raise ValueError("each input must be an integer prime from 2 to 31")
    if len(set(primes)) != len(primes) or not all(is_prime(p) for p in primes):
        raise ValueError("inputs must be distinct primes")
    number = prod(primes) + 1
    return number, prime_factors(number)


def main() -> None:
    for primes in ([2, 3], [2, 3, 5, 7, 11, 13], [3, 5]):
        number, factors = euclid_example(primes)
        print(f"primes={primes}")
        print(f"product+1={number}; prime_factors={factors}")
        print(f"all factors outside input: {set(factors).isdisjoint(primes)}")
        print()
    print("Finite examples only; see the written proof in the guide.")


if __name__ == "__main__":
    main()
