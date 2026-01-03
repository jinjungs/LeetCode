from typing import List


class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        count_one = sum(nums)
        if count_one <= 1:
            return count_one

        one_idx = -1
        count_zero = 0

        res = 1
        m = 10**9 + 7

        # don't count the zeros before the first one comes
        for i, num in enumerate(nums):
            if num == 1:
                if one_idx != -1:
                    res = res * (count_zero + 1) % m
                one_idx = i
                count_zero = 0
            else:
                count_zero += 1

        return res

