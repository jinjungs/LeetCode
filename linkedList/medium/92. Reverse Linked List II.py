# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)

        # Step1: reach node at position "left"
        prevLeft, cur = dummy, head
        for _ in range(left-1):
            prevLeft = cur
            cur = cur.next

        # Step2: reverse
        prev = None
        for _ in range(right-left+1):
            tempNext = cur.next
            cur.next = prev
            prev = cur
            cur = tempNext

        # Step3: repoint the Node
        prevLeft.next.next = cur
        prevLeft.next = prev

        return dummy.next
        