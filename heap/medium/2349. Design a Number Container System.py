from collections import defaultdict
from heapq import heappush, heappop
class NumberContainers:

    def __init__(self):
        self.numberMap = defaultdict(list) # key: number, value: index list
        self.indexMap = {} # key: index, value: number

    def change(self, index: int, number: int) -> None:
        self.indexMap[index] = number
        heappush(self.numberMap[number], index)

    def find(self, number: int) -> int:
        if number not in self.numberMap:
            return -1

        heap = self.numberMap[number]

        # lazy deletion
        while heap:
            idx = heap[0]
            if self.indexMap.get(idx) == number:
                return idx
            heappop(heap)

        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)