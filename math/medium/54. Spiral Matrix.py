from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        visited = [[False] * m for _ in range(n)]
        d = [(0,1), (1,0), (0,-1), (-1,0)]
        x = y = dn = 0
        res = []
        
        for _ in range(n * m):
            res.append(matrix[x][y])
            visited[x][y] = True

            nx, ny = d[dn][0] + x, d[dn][1] + y
            if (nx < 0 or ny < 0 or nx >= n or ny >= m) or visited[nx][ny]:
                dn = (dn + 1) % 4
                nx, ny = d[dn][0] + x, d[dn][1] + y
            x, y = nx, ny

        return res
