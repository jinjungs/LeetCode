# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1. Brute Force
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        new_head = ListNode()
        res = new_head

        while lists:
            # get min
            min_val = float('inf')
            min_idx = -1
            for i, head in enumerate(lists):
                if head and head.val <= min_val:
                    min_val = head.val
                    min_idx = i
            if min_val == float('inf'):
                break

            next_node = lists[min_idx]
            lists[min_idx] = lists[min_idx].next
            new_head.next = next_node
            new_head = new_head.next

        return res.next

# 2. Using Min Heap
from heapq import heappush, heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        h = []
        for i, node in enumerate(lists):
            if node:
                heappush(h, (node.val, i, node))

        head = ListNode()
        dummy = head
        while h:
            val, idx, node = heappop(h)
            head.next = node
            head = head.next
            if node.next:
                heappush(h, (node.next.val, idx, node.next))

        return dummy.next
