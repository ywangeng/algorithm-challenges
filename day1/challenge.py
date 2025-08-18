"""
Question:

You are given a string consisting of the letters x and y, such as xyxxxyxyy.
In addition, you have an operation called flip, which changes a single x to y or vice versa.

Determine how many times you would need to apply this operation to ensure that all x's come before all y's.
In the preceding example, it suffices to flip the second and sixth characters, so you should return 2.
"""


def solution(s: str) -> int:
    n = len(s)

    # Precompute counts of x's and y's
    prefix_y = [0] * (n + 1)  # prefix_y[i] = number of 'y' in s[:i]
    for i in range(1, n + 1):
        prefix_y[i] = prefix_y[i - 1] + (1 if s[i - 1] == 'y' else 0)

    suffix_x = [0] * (n + 1)  # suffix_x[i] = number of 'x' in s[i:]
    for i in range(n - 1, -1, -1):
        suffix_x[i] = suffix_x[i + 1] + (1 if s[i] == 'x' else 0)

    # Try every split point
    ans = float("inf")
    for i in range(n + 1):
        flips = prefix_y[i] + suffix_x[i]
        ans = min(ans, flips)

    return ans


print(solution("xyxxxyxyy"))  # Output: 2
