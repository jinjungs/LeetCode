# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head = head
        prev = None

        # reverse order
        while new_head:
            temp = new_head.next
            new_head.next = prev
            prev = new_head
            new_head = temp

        new_head = prev
        prev = None
        num = 1

        while new_head:
            temp = new_head.next
            # delete
            if num == n:
                new_head.next = None
            # reverse order
            else:
                new_head.next = prev
                prev = new_head
                
            new_head = temp
            num += 1

        return prev
