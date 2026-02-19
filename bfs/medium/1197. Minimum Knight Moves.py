from collections import deque

# BFS
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)

        d = [(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)]

        # Bound the search area
        min_x, max_x = -2, x + 2
        min_y, max_y = -2, y + 2

        steps = 0
        q = deque([(0,0)])
        visited = {(0,0)}

        while q:            
            for _ in range(len(q)):
                r, c = q.popleft()
                if x == r and c == y:
                    return steps

                for dr, dc in d:
                    nr, nc = dr + r, dc + c
                    if not (min_x <= nr <= max_x and min_y <= nc <= max_y):
                        continue
                    if (nr, nc) in visited:
                        continue
                    visited.add((nr,nc))
                    q.append((nr,nc))

            steps += 1

        return -1
