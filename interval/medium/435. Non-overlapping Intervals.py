from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: pair[1])
        lastEnd = intervals[0][1]
        res = 0

        for start, end in intervals[1:]:
            if lastEnd <= start:
                lastEnd = end
            else:
                res += 1

        return res
