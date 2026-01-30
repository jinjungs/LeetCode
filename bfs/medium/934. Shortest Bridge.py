from collections import deque
from typing import List
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # 1. mark first island '#'
        # put edges of island to q
        # how to know edges? in 4 directions contain water
        # when meets the other island, return

        n = len(grid)
        dx, dy = [1,0,-1,0], [0,1,0,-1]
        q = deque()

        def dfs(x, y):
            grid[x][y] = 2
            q.append((x, y))
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                    dfs(nx, ny)
        
        # 1) Find and mark the first island
        found = False
        for r in range(n):
            if found:
                break
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break

        # 2) Multi-source BFS from the whole first island
        flips = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            return flips
                        elif grid[nx][ny] == 0:
                            grid[nx][ny] = 2
                            q.append((nx,ny))
            flips += 1

        return -1
