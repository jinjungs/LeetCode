import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q, self.k = nums, k
        heapq.heapify(self.q)
        while len(self.q) > k:
            heapq.heappop(self.q)

    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)
        if len(self.q) > self.k:
            heapq.heappop(self.q)
        return self.q[0]
