
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # old to new
        h = {}
        curr = head
        while curr:
            h[curr] = Node(curr.val)
            curr = curr.next

        # fill next and random
        curr = head
        while curr:
            h[curr].random = h.get(curr.random)
            h[curr].next = h.get(curr.next)
            curr = curr.next
        
        return h[head]

        