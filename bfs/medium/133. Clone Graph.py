# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
from collections import deque


# 1. BFS
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {node: Node(node.val)}
        q = deque([node])

        while q:
            curr = q.popleft()
            for nei in curr.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val)
                    q.append(nei)
                visited[curr].neighbors.append(visited[nei])

        return visited[node]        

# 2. DFS
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}

        def dfs(curr):
            if curr in visited:
                return visited[curr]

            new_node = Node(curr.val)            
            visited[curr] = new_node
            
            for nei in curr.neighbors:                
                new_node.neighbors.append(dfs(nei))

            return new_node

        return dfs(node)