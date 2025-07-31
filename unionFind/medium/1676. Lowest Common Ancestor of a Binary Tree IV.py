from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if len(nodes) == 1:
            return nodes[0]

        parent = {}
        def union(x, y):
            ancestors_x = set()
            while x != root:
                ancestors_x.add(x)
                x = parent[x]
            ancestors_x.add(root)

            while y not in ancestors_x:
                y = parent[y]
            return y

        def dfs(node: TreeNode, p: TreeNode):
            parent[node] = p
            if node.left:
                dfs(node.left, node)
            if node.right:
                dfs(node.right, node)

        dfs(root, root)

        prev = nodes[0]
        for i in range(1, len(nodes)):
            lca = union(prev, nodes[i])
            prev = lca

        return prev
        
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        node_set = set(nodes)

        def dfs(node):
            if not node:
                return None
            if node in node_set:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            return left or right

        return dfs(root)
        