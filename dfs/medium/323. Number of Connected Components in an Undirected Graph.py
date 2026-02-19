from typing import List


# DFS
class Solution:
    def connectedComponents(self, n: int, edges: List[int]) -> int:
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node: int) -> None:
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        visited = set()
        res = 0

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                res += 1

        return res
