from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        res = 0 

        def min_swaps(arr):
            sorted_arr = sorted(l)
            pos = {v:i for i, v in enumerate(arr)} # current index of each value
            swaps = 0

            for i in range(len(arr)):
                correct_val = sorted_arr[i]
                if arr[i] == correct_val:
                    continue
                
                j = pos[correct_val] # where the correct value currently is

                pos[arr[i]] = j
                pos[arr[j]] = i
                arr[i], arr[j] = arr[j], arr[i]

                swaps += 1
            
            return swaps 

        while q:
            l = []
            for _ in range(len(q)):
                node = q.popleft()
                l.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res += min_swaps(l)

        return res