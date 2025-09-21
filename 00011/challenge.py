"""
Question:

Given a complete binary tree, count the number of nodes in faster than O(n) time.
Recall that a complete binary tree has every level filled except the last,
and the nodes in the last level are filled starting from the left.
"""


class TreeNode:
    __slots__ = ("val", "left", "right")

    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def solution(root: TreeNode) -> int:
    def left_height(node):
        h = 0
        while node:
            h += 1
            node = node.left
        return h

    def right_height(node):
        h = 0
        while node:
            h += 1
            node = node.right
        return h

    def count(node):
        if not node:
            return 0
        hl = left_height(node)
        hr = right_height(node)
        if hl == hr:
            return (1 << hl) - 1
        return 1 + count(node.left) + count(node.right)

    return count(root)
