from typing import List


class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        # early return
        prod = 1
        for num in nums:
            prod *= num

        if prod != target * target:
            return False

        nums.sort(reverse=True)
        
        # backtracking
        def dfs(idx: int, total: int):
            if target % total != 0: 
                return False
                
            if total == target:
                return True

            if total > target:
                return False

            for j in range(idx + 1, n):
                total *= nums[j]
                if dfs(j, total):
                    return True
                total //= nums[j]

            return False
                
        return dfs(0, nums[0])
