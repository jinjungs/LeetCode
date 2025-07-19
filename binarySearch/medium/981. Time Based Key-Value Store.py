from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time:
            return ""

        arr = self.time[key]
        l, r = 0, len(arr)-1
        res = ''

        while l <= r:
            mid = (l+r) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                l = mid+1                                
            else:
                r = mid-1
                
        return res
