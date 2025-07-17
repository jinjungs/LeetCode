from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def isEdge(x,y)-> bool:
            return x < 0 or y < 0 or x >= ROWS or y >= COLS

        fresh = 0
        q = deque()
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 1:
                    fresh += 1
                elif grid[x][y] == 2:
                    q.append([x,y])

        time = 0
        dx, dy = [0,1,0,-1], [1,0,-1,0]
        while q and fresh > 0:
            for _ in range(len(q)):
                x, y = q.popleft()
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if not isEdge(nx,ny) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append([nx,ny])
            time += 1

        return -1 if fresh > 0 else time
