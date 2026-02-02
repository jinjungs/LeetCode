from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def solve(l, r, s) -> int:
            memo = [[-1] * n for _ in range(n)]

            def dfs(l, r) -> int:
                if l >= r:
                    return 0

                if memo[l][r] != -1:
                    return memo[l][r]
                
                best = 0
                if l + 1 <= r and nums[l] + nums[l+1] == s:
                    best = max(best, 1 + dfs(l+2, r))
                if r - 1 > l and nums[r-1] + nums[r] == s:
                    best = max(best, 1 + dfs(l, r-2))
                if nums[l] + nums[r] == s:
                    best = max(best, 1 + dfs(l+1, r-1))

                memo[l][r] = best
                return best

            return dfs(l, r)
            
        return max(
            1 + solve(2, n-1, nums[0] + nums[1]), 
            1 + solve(0, n-3, nums[n-2] + nums[n-1]), 
            1 + solve(1, n-2, nums[0] + nums[n-1])
        )