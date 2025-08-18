from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # check if the parent is same.
        n = len(edges)
        parent = [i for i in range(n+1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y) -> bool:
            px = find(x)
            py = find(y)
            if px == py:
                return False
            parent[py] = px
            return True
        
        for a,b in edges:
            if not union(a,b):
                return [a,b]
        