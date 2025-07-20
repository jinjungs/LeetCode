from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        dx, dy = [0,1,0,-1], [1,0,-1,0]

        def dfs(x, y) -> int:
            if (x<0 or y<0 or x>=ROWS or y>=COLS) or grid[x][y] != 1:
                return 0

            grid[x][y] = -1
            cnt = 1
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                cnt += dfs(nx,ny)
            return cnt

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    res = max(res, dfs(i,j))

        return res