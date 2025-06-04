from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        self.backtrack(nums, target, 0, [], res)
        return res

    def backtrack(self, nums: List[int], target: int, start:int, path: List[int], res:List[List[int]]):
        if target == 0:
            res.append(path.copy())
            return 
        for i in range(start, len(nums)):
            if nums[i] > target:
                break
            path.append(nums[i])
            self.backtrack(nums, target - nums[i], i, path, res)
            path.pop()
        