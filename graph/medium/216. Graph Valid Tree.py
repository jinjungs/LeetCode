from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        # cycle detection
        node_map = defaultdict(list)
        for u,v in edges:
            node_map[u].append(v)
            node_map[v].append(u)

        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for next_node in node_map[node]:
                if next_node == prev:
                    continue
                if not dfs(next_node, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n