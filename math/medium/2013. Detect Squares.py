from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self.ptCount = defaultdict(int)
        self.points = []
        
    def add(self, point: List[int]) -> None:
        self.ptCount[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptCount[(x, py)] * self.ptCount[(px, y)]
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)