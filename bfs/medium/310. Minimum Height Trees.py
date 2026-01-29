from collections import defaultdict, deque
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        degree = [0] * n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1

        q = deque([i for i in range(n) if degree[i] == 1])

        remaining = n
        while remaining > 2:
            layer_size = len(q)
            remaining -= layer_size

            for _ in range(layer_size):
                leaf = q.popleft()
                for nei in graph[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)

        return list(q)
