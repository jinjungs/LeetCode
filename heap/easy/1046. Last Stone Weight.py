import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stone = [-stone for stone in stones]
        heapq.heapify(new_stone)

        while len(new_stone) > 1:
            one = -heapq.heappop(new_stone)
            two = -heapq.heappop(new_stone)
            if one > two:
                heapq.heappush(new_stone, two-one)

        return 0 if not new_stone else -new_stone[0]
