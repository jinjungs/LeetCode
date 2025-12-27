from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        res = [[0] * COLS for _ in range(ROWS)]
        dx, dy = [0,1,0,-1], [1,0,-1,0]
        visited = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r,c,0))
                    visited.add((r,c))

        while q:
            x, y, dist = q.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx >= 0 and ny >=0 and nx < ROWS and ny < COLS and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    new_dist = 0 if mat[nx][ny] == 0 else dist + 1
                    res[nx][ny] = new_dist
                    q.append((nx,ny,new_dist))

        return res