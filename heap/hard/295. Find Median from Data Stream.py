import heapq
class MedianFinder:

    def __init__(self):
        self.lo = [] # max-heap       
        self.hi = [] # min-heap

    def addNum(self, num: int) -> None:
        if len(self.lo) == 0 or -self.lo[0] > num:
            heapq.heappush(self.lo, -num)
        else:
            heapq.heappush(self.hi, num)

        if len(self.lo) > len(self.hi) + 1:
            heapq.heappush(self.hi, -heapq.heappop(self.lo))
        elif len(self.hi) > len(self.lo) + 1:
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        elif len(self.lo) < len(self.hi):
            return self.hi[0]
        else:
            return (-self.lo[0] + self.hi[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
