from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        res = 0

        n = len(nums)
        for i in range(n-2):
            l, r = i+1, n-1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if abs(threeSum - target) < diff:
                    res = threeSum
                    diff = abs(threeSum - target)
                if threeSum < target:
                    l += 1
                elif threeSum > target:
                    r -= 1
                else:
                    return threeSum

        return res
