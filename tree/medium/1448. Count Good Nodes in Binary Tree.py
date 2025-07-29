# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        good = [0]        
        def dfs(prevMax:int, node: TreeNode):
            if node.val >= prevMax:
                good[0] += 1
                prevMax = max(node.val, prevMax)
            if node.left:
                dfs(prevMax, node.left)
            if node.right:
                dfs(prevMax, node.right)

        dfs(-float('inf'), root)
        return good[0]