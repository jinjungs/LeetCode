from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0

        # repeat k+1 cause we can use k+1 edges
        for _ in range(k + 1):
            # copy previous result (prevent updates in the same round)
            # in 1st round, max use 1 edge
            # in 2nd round, max use 2 edge
            tmp = dist[:]
            for u, v, w in flights:
                if dist[u] != INF and dist[u] + w < tmp[v]:
                    tmp[v] = dist[u] + w
            dist = tmp

        return -1 if dist[dst] == INF else dist[dst]