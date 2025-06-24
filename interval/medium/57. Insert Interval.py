from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = len(intervals) -1
        new_start, new_end = newInterval[0], newInterval[1]
        merge_list = []
        result = []

        def merge(l1: List[int], l2: List[int]) -> List[int]:
            return [min(l1[0], l2[0]), max(l1[1], l2[1])]

        def isOverlap(interval: List[int], merged: List[int]) -> bool:
            start, end = interval[0], interval[1]
            m_start, m_end = merged[0], merged[1]
            return start <= m_end or end <= m_start

        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]

            # consider not overlapping intervals
            if start > new_end or end < new_start:
                result.append(intervals[i])
                continue

            # consider overlapping intervals
            if len(merge_list) == 0:
                if isOverlap(intervals[i], newInterval):
                    merge_list = merge(newInterval, intervals[i])
                    result.append(merge_list)
            else:
                if isOverlap(intervals[i], merge_list):
                    result.pop()
                    merge_list = merge(merge_list, intervals[i])
                    result.append(merge_list)

        if len(merge_list) == 0:
            result.append(newInterval)
            result.sort()

        return result

# 25/06/23 
class Solution2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):
            s, e = interval[0], interval[1]
            ns, ne = newInterval[0], newInterval[1]
            if e < ns:
                res.append(interval)
            elif ne < s:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [min(s,ns), max(e,ne)]

        res.append(newInterval)
        return res
            