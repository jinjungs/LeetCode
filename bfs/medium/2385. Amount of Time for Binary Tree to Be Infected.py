from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return 0

        parent = {}
        startNodeList = [None]

        def dfs(node, par):
            if not node:
                return

            if node.val == start:
                startNodeList[0] = node

            parent[node] = par

            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        # spread out from infected node -> BFS
        startNode = startNodeList[0]
        visited = {startNode}
        q = deque([startNode])
        minute = 0

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for nei in (node.left, node.right, parent[node]):
                    if nei and nei not in visited:
                        visited.add(nei)
                        q.append(nei)

            if q:
                minute += 1

        return minute

