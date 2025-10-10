"""
Question:

The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. The method is to take
increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two),
then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N,
the unmarked numbers that remain will be prime.
"""


def solution(n):
    if n < 2:
        return []

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        for multiple in range(i * i, n, i):
            is_prime[multiple] = False

    return [i for i, prime in enumerate(is_prime) if prime]


print(solution(100))
