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
