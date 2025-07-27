from collections import defaultdict
from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * n  # Discovery times
        low = [-1] * n   # Low values
        time = [0]
        res = []

        def dfs(u, parent):
            disc[u] = low[u] = time[0]
            time[0] += 1
            for v in graph[u]:
                if v == parent:
                    continue
                if disc[v] == -1:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:  # Bridge condition
                        res.append([u, v])
                else:
                    low[u] = min(low[u], disc[v])

        dfs(0, -1)
        return res