# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, output):
            if not root:
                return
            output.append(root.val)
            dfs(root.left, output)
            dfs(root.right, output)

        output = []
        dfs(root, output)
        return output
