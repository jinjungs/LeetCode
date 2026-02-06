from typing import List
from collections import defaultdict

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        res = [0] * n

        def dfs(node: int, parent: int) -> List[int]:
            # counts[c] = number of nodes with label (chr(c + 'a')) in this subtree
            counts = [0] * 26

            for nei in graph[node]:
                if nei == parent:
                    continue
                child_counts = dfs(nei, node)
                for i in range(26):
                    counts[i] += child_counts[i]

            idx = ord(labels[node]) - ord('a')
            counts[idx] += 1
            res[node] = counts[idx]
            return counts

        dfs(0, -1)
        return res