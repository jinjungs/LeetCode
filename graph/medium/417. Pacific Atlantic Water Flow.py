from typing import List


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
