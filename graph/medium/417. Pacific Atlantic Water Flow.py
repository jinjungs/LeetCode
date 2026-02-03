from typing import List
from collections import deque

# DFS
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        X, Y = len(heights), len(heights[0])
        pacific = [[False] * Y for _ in range(X)]
        atlantic = [[False] * Y for _ in range(X)]
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]

        def dfs(x, y, visited, prev):
            if x<0 or y<0 or x>=X or y>=Y:
                return
            if visited[x][y] or heights[x][y] < prev:
                return
            visited[x][y] = True
            for i in range(4):
                dfs(x+dx[i], y+dy[i], visited, heights[x][y])

        for i in range(X):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, Y-1, atlantic, heights[i][Y-1])
        for j in range(Y):
            dfs(0, j, pacific, heights[0][j])
            dfs(X-1, j, atlantic, heights[X-1][j])

        res = []
        for i in range(X):
            for j in range(Y):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i,j])

        return res


# BFS
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        dx, dy = [0,1,0,-1], [1,0,-1,0]        

        def bfs(starts):
            reachable = [[False] * COLS for _ in range(ROWS)]
            q = deque()

            for r, c in starts:
                if not reachable[r][c]:
                    reachable[r][c] = True
                    q.append((r,c))

            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < ROWS and 0 <= ny < COLS and not reachable[nx][ny] and heights[nx][ny] >= heights[x][y]:
                        reachable[nx][ny] = True
                        q.append((nx,ny))

            return reachable

        # pacific
        pacific_starts = [(r, 0) for r in range(ROWS)] + [(0, c) for c in range(1, COLS)]
        atlantic_starts = [(r, COLS-1) for r in range(ROWS)] + [(ROWS-1, c) for c in range(COLS-1)]

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r,c])

        return res
                