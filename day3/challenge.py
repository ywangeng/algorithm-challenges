"""
Question:

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0, head)
    fast = slow = dummy

    # Move fast k+1 steps ahead
    for _ in range(k + 1):
        fast = fast.next

    # Move both until fast reaches end
    while fast:
        fast = fast.next
        slow = slow.next

    # Delete kth last node
    slow.next = slow.next.next

    return dummy.next
