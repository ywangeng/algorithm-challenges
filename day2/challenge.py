"""
Question:

Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.

"""

from collections import Counter


def solution(w: str, s: str):
    n, m = len(s), len(w)
    if m > n:
        return []

    need = Counter(w)  # target char counts
    window = Counter(s[:m])  # counts for first window
    ans = []

    if window == need:
        ans.append(0)

    # slide the window over S
    for i in range(m, n):
        in_ch = s[i]
        out_ch = s[i - m]

        window[in_ch] += 1
        window[out_ch] -= 1
        if window[out_ch] == 0:
            del window[out_ch]  # keep Counter sizes comparable

        if window == need:
            ans.append(i - m + 1)

    return ans


print(solution("ab", "abxaba"))  # [0, 3, 4]
