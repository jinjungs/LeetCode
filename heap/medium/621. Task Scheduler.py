import heapq
from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [-cnt for cnt in counter.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown = deque() # (available_time, count)

        while max_heap or cooldown:
            time += 1
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1 # minus count after pop
                if cnt !=0:
                    cooldown.append((time + n, cnt)) # after n seconds possible

            if cooldown and cooldown[0][0] == time:
                heapq.heappush(max_heap, cooldown.popleft()[1])

        return time