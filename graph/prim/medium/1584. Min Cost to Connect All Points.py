from ast import List
from heapq import heappop, heappush
from math import inf
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # MST - Prim
        n = len(points)
        visited = [False] * n        
        best = [inf] * n
        best[0] = 0

        q = [(0, 0)] # distance, vertax
        total = 0
        visited_count = 0

        while q and visited_count < n:
            d, idx = heappop(q)
            if visited[idx]:
                continue
            visited[idx] = True
            visited_count += 1
            total += d

            # put all nodes and the distance 
            x, y = points[idx]
            for ni, (nx,ny) in enumerate(points):
                if not visited[ni]:
                    nd = abs(x-nx) + abs(y-ny)
                    if nd < best[ni]:
                        best[ni] = nd
                        heappush(q, (nd, ni))

        return total