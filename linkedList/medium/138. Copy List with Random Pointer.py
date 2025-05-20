
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

        d = dict()

        d_head = Node(head.val, head.next, head.random)
        d[head] = d_head
        return_head = d_head

        # put in dict
        while head and head.next:            
            head = head.next
            new_next_head = Node(head.val, head.next, head.random)

            d[head] = new_next_head            
            d_head.next = new_next_head
            d_head = d_head.next            
            
        d_head = return_head

        # copy next, random
        while d_head:
            d_head.random = None if not d_head.random else d.get(d_head.random)
            d_head = d_head.next

        return return_head

        