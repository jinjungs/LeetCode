# Definition for a binary tree node.
import copy

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # BFS
        queue = []
        queue.append([[], root])
        pa, qa = [], []

        while queue and (not pa or not qa):
            a, node = queue.pop()
            na = copy.deepcopy(a)
            na.append(node.val)
            if node.val == p.val:
                pa = na
            if node.val == q.val:
                qa = na
            if node.left:
                queue.append([na, node.left])
            if node.right:
                queue.append([na, node.right])

        res = None
        for i in range(min(len(pa), len(qa))):
            if pa[i] == qa[i]:
                res = int(pa[i])
            else:
                break

        # find TreeNode
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop()
            if node.val != res:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                return node
