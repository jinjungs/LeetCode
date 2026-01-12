from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # fixed window k
        n = len(arr)
        l = 0

        for r in range(k, n):
            a, b = abs(arr[l] - x), abs(arr[r] - x)
            if a < b or (a == b and arr[l] < arr[r]):
                return arr[l:r]
            l += 1

        return arr[l:]
