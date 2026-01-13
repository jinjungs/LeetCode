from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (-p[0], p[1]))
        n = len(points)
        res = 0

        for i in range(n):
            y = float('inf')

            for j in range(i + 1, n):
                if y > points[j][1] >= points[i][1]:
                    res += 1
                    y = points[j][1]

        return res