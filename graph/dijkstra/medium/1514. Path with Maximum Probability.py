from collections import defaultdict
import heapq
from typing import List
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        g = defaultdict(list)
        for (a,b), p in zip(edges, succProb):
            g[a].append((b,p))
            g[b].append((a,p))

        success = [0.0] * n
        success[start_node] = 1.0

        q = [(-1, start_node)]
        while q:
            s, node = heapq.heappop(q)
            s *= -1
            if s < success[node]:
                continue

            for next_node, next_val in g[node]:                
                nv = s * next_val
                if nv > success[next_node]:
                    success[next_node] = nv
                    heapq.heappush(q, (-nv, next_node))

        return success[end_node]
