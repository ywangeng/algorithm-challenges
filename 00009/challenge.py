"""
Question:

Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".

"""


def solution(s: str) -> str:
    if not s:
        return ''

    start, end = 0, 0

    def expand(lt: int, rt: int):
        while lt >= 0 and rt < len(s) and s[lt] == s[rt]:
            lt -= 1
            rt += 1

        return lt + 1, rt - 1

    for i in range(len(s)):
        lt1, rt1 = expand(i, i)

        lt2, rt2 = expand(i, i + 1)

        if rt1 - lt1 > end - start:
            start, end = lt1, rt1

        if rt2 - lt2 > end - start:
            start, end = lt2, rt2

    return s[start: end + 1]
