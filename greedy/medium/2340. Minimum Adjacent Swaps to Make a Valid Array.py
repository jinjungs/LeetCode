from typing import List


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        maxNum = max(nums)
        minNum = min(nums)
        minIndex = maxIndex = 0

        for i in range(n):
            if nums[i] == minNum:
                minIndex = i
                break

        for j in range(n-1, -1, -1):
            if nums[j] == maxNum:
                maxIndex = j
                break

        # min, max
        if minIndex <= maxIndex:
            return minIndex + (n-1-maxIndex)
        # max, min
        else:
            return (minIndex) + (n-1-maxIndex) - 1
