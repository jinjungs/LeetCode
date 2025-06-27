# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, output):
            if not root:
                return 
            dfs(root.left, output)
            output.append(root.val)
            dfs(root.right, output)
                    
        output = []
        dfs(root, output)
        return output
