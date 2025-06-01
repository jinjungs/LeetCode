import math
import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        # heapq.heapify(closest) # not needed

        for point in points:
            dist = self.getDistance(point[0], point[1])
            heapq.heappush(closest, (-dist, point))
            if len(closest) > k:
                heapq.heappop(closest)
        return [x[1] for x in closest]

    def getDistance(self, x, y):
        return math.sqrt(x*x + y*y)