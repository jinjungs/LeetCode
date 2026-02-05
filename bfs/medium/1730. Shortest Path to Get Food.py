from typing import List
from collections import deque

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '*':
                    grid[r][c] = 'X'
                    q.append((r,c))
                    break
        
        steps = 0
        dx, dy = [1,0,-1,0], [0,1,0,-1]
        while q:
            x, y = q.popleft()
            steps += 1
            for _ in range(len(q)):
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < ROWS and 0 <= ny < COLS:
                        cell = grid[nx][ny]
                        if cell == '#':
                            return steps
                        elif cell == 'O':
                            grid[nx][ny] = 'X'
                            q.append((nx,ny))
        
        return -1
    