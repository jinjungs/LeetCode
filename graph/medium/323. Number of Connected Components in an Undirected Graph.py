from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for u, v in edges:
            d[u].append(v)
            d[v].append(u)

        visit = set()
        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for new_node in d[node]:
                if new_node == prev:
                    continue
                dfs(new_node, node)
            return True
            
        res = 0
        for i in range(n):
            if dfs(i, -1):
                res += 1

        return res