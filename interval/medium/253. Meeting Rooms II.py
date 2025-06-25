# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda pair: pair.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)
