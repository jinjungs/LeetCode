from collections import defaultdict
import heapq
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        INF = float('inf')
        dist = [INF] * (n+1)
        dist[k] = 0

        q = [(0,k)] # accumulated_distance, node
        while q:
            d, u = heapq.heappop(q)
            if d > dist[u]:
                continue
            
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(q, (nd, v))
        
        res = max(dist[1:])
        return -1 if res == INF else res

