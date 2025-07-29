# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        def dfs(node) -> int:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            diameter[0] = max(diameter[0], left + right)
            return max(left, right) + 1

        dfs(root)
        return diameter[0]