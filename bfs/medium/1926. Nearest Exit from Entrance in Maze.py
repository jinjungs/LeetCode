from collections import deque
from typing import List
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS = len(maze)
        COLS = len(maze[0])
        dx, dy = [0,1,0,-1], [1,0,-1,0]

        visited = [[False] * COLS for _ in range(ROWS)]
        visited[entrance[0]][entrance[1]] = True

        q = deque([(entrance[0], entrance[1], 0)])

        while q:
            x, y, val = q.popleft()

            # border
            if (x == 0 or y == 0 or x == ROWS-1 or y == COLS-1) and val > 0:
                return val

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < ROWS and 0 <= ny < COLS and not visited[nx][ny] and maze[nx][ny] == '.':
                    visited[nx][ny] = True
                    q.append((nx, ny, val + 1))

        return -1
