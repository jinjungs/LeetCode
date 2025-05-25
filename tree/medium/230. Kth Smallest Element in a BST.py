from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # dfs
        res = []
        self.dfs(root, res)
        return res[k-1]

    def dfs(self, node, l: list) -> None:
        if not node:
            return
        self.dfs(node.left, l) 
        l.append(node.val)
        self.dfs(node.right, l)
