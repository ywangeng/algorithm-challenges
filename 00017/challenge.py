"""
Question:

A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements,
return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.
"""


def solution(arr: list):
    if not arr:
        return False

    for i, v in enumerate(l):
        if i == v:
            return i

    return False


def solution2(arr: list):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left - (left - right) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1

    return False


print(solution2([-6, 0, 2, 40]))
