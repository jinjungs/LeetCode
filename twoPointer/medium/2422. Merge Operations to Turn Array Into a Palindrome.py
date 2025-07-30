from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, len(nums)-1

        while l < r:
            while l < r and nums[l] != nums[r]:
                if nums[l] < nums[r]:
                    l += 1
                    nums[l] += nums[l-1]
                else:
                    r -= 1
                    nums[r] += nums[r+1]
                res += 1

            l += 1
            r -= 1

        return res