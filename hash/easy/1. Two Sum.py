from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Test all cases: O(n^2)
        # for i in range(len(nums)):
        #     for j in range(1,len(nums)):
        #         if i!= j and nums[i] + nums[j] == target:
        #             return [i,j]

        # Hashmap: O(n)
        d = dict() # val -> index
        for i, num in enumerate(nums):
            if target - num in d:
                return [d.get(target - num), i]
            d[num] = i