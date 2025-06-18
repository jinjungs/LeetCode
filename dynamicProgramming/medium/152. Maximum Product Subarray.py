from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = curr_min = curr_max = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            if n < 0:
                curr_min, curr_max = curr_max, curr_min

            curr_min = min(n, curr_min * n)
            curr_max = max(n, curr_max * n)

            res = max(res, curr_max)

        return res
