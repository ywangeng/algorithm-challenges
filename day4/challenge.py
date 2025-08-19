"""
Question:

Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability,
implement a function rand5() that returns an integer from 1 to 5 (inclusive).
"""

import random


def rand7():
    return random.randint(1, 7)


# P(accept) = 5 / 7 = 71.4%
# P(reject) = 28.6%
def solution1():
    while True:
        r = rand7()

        if r <= 5:
            return r


# P (accept) = 45/49 = 91.8%
# P (reject) = 8.2%
def solution2():
    while True:
        num = (rand7() - 1) * rand7() + rand7()  # uniform in 1 - 49

        if num <= 45:
            return (num - 1) % 5 + 1
