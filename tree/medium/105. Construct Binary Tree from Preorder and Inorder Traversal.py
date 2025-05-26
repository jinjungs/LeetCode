
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        headVal = preorder[0]
        head = TreeNode(headVal)

        # find the index of the root in inorder traversal
        idx = inorder.index(headVal)

        head.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        head.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
            
        return head
