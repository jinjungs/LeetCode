from collections import defaultdict
from math import inf
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # floyd-warshall
        dist = [[inf] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for a,b,w in edges:
            dist[a][b] = w
            dist[b][a] = w

        for k in range(n):
            for i in range(n):
                dik = dist[i][k]
                if dik == inf:
                    continue
                for j in range(n):
                    if dik + dist[k][j] < dist[i][j]:
                        dist[i][j] = dik + dist[k][j]

        # count cities at most distanceThreshold
        count_cities = [0] * n
        for i in range(n):
            for j in range(i+1, n):
                if dist[i][j] <= distanceThreshold:
                    count_cities[i] += 1
                    count_cities[j] += 1
        
        min_values = min(count_cities)
        for i in range(n-1, -1, -1):
            if count_cities[i] == min_values:
                return i


