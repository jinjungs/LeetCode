from collections import deque
from typing import List
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        HOR = len(rooms)
        VER = len(rooms[0])
        dx, dy = [-1,0,1,0], [0,-1,0,1]
        q = deque()

        for i in range(HOR):
            for j in range(VER):
                if rooms[i][j] == 0:
                    q.append([i,j,0])

        while q:
            x, y, v = q.popleft()
            if rooms[x][y] != 0 and rooms[x][y] != INF:
                continue
            rooms[x][y] = v
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (0<=nx<HOR and 0<=ny<VER) and rooms[nx][ny] == INF:
                    q.append([nx,ny,v+1])
