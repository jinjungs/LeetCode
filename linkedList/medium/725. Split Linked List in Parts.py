# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = []

        # count total number of node
        total = 0
        curr = head
        while curr:
            total += 1
            curr = curr.next

        # calculate how many node should be in output
        q, r = total // k, total % k

        # put node in output
        curr = head
        for i in range(k):
            count = q+1 if i < r else q
            new_head = curr
            prev = None
            
            for c in range(count):
                prev = curr
                if curr:
                    curr = curr.next

            # split tail
            if prev:
                prev.next = None

            res.append(new_head)

        return res
        