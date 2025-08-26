from typing import List
from math import inf

class Solution:
    # DP - original solution
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [inf] * n
        dp[0] = 0

        for i in range(n-1):
            for j in range(nums[i]+1):
                if i + j >= n:
                    break
                dp[i+j] = min(dp[i+j], dp[i] + 1)

        return dp[-1]

    # Greedy(BFS) - use less memory solution
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0 
        res = 0

        while r < n - 1:
            far = 0
            for i in range(l, r+1):
                far = max(far, i + nums[i])
            l = r+1
            r = far
            res += 1

        return res

