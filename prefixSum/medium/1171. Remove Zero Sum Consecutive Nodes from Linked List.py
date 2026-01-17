# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        curr = dummy
        h = {}
        total = 0

        while curr:
            total += curr.val
            h[total] = curr
            curr = curr.next
        
        # 같은 prefixSum이 두 번 나오면, 그 사이 합은 0
        curr = dummy
        total = 0
        while curr:
            total += curr.val
            curr.next = h[total].next
            curr = curr.next

        return dummy.next