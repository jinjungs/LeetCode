from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # remains
        n = len(nums)
        val_arr = [0] * value

        for i in range(n):
            val_arr[nums[i] % value] += 1

        idx = 0
        while val_arr[idx % value] > 0:
            val_arr[idx % value] -= 1
            idx += 1

        return idx
