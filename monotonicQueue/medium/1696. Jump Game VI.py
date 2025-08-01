from collections import deque

"""
[1,-1,-2,4,-7,3]
[1]
[1,0] -> length max k == 2
  [0,-1]
  [0,-1,4] -> [4]
        [4, -3]
             [7]


[1,-5,-20,4,-1,3,-6,-3],
1
1,-4
1,-4,-19
1,-4,-19,0


[100,-1,-100,-1,100]
100
100 99
100 99 0
100 99 98
198

"""

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        monotonic_queue = deque()

        for i,num in enumerate(nums):
            # not length of monotonic_queue is bigger than k... the diff between index is bigger than k!!
            # if len(monotonic_queue) > k:
            if monotonic_queue and monotonic_queue[-1][0] - monotonic_queue[0][0] >= k:
                monotonic_queue.popleft()
            nextSum = num if i == 0 else monotonic_queue[0][1] + num
            while monotonic_queue and monotonic_queue[-1][1] <= nextSum:
                monotonic_queue.pop()
            monotonic_queue.append([i,nextSum])

        return monotonic_queue[-1][1]