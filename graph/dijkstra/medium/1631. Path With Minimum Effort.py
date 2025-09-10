from math import inf
from heapq import heappush, heappop
from typing import List
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        dx, dy = [0,1,0,-1], [1,0,-1,0]
        dist = [[inf] * COLS for _ in range(ROWS)]
        dist[0][0] = 0
        
        q = [[0,0,0]]

        while q:
            effort, x, y = heappop(q)     
            # Early exit: the first time we pop the target, it's optimal
            if x == ROWS - 1 and y == COLS - 1:
                return effort
            if effort > dist[x][y]:
                continue

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0<=nx<ROWS and 0<=ny<COLS:
                    new_effort = max(abs(heights[x][y] - heights[nx][ny]), effort)
                    if new_effort < dist[nx][ny]:
                        dist[nx][ny] = new_effort
                        heappush(q, [new_effort,nx,ny])

        return dist[-1][-1]