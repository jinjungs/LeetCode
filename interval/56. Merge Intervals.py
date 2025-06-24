from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        result = []
        for interval in intervals:
            if len(result) ==0:
                result.append(interval)
                continue
            r = result[-1]
            if interval[0] <= r[1]:
                result.pop()
                result.append([r[0], max(r[1], interval[1])])
            else:
                result.append(interval)

        return result
    
# 25/06/24
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            lastEnd = res[-1][1]

            if lastEnd < start:
                res.append(intervals[i])
            else:
                # Intervals are sorted, so once overlapping is confirmed,
                # we only need to update the end of the last interval.
                res[-1][1] = max(end, lastEnd)

        return res
