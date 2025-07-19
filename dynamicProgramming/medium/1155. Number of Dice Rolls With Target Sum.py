from typing import List


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [[-1] * (target + 1) for _ in range(n + 1)]
        return self.dfs(n, k, target, dp, MOD)

    def dfs(self, n: int, k: int, target: int, dp: List[List[int]], MOD: int) -> int:
        if target < 0:
            return 0
        if n == 0:
            return 1 if target == 0 else 0
        
        if dp[n][target] != -1:
            return dp[n][target]

        res = 0
        for num in range(1, k + 1):
            res += self.dfs(n - 1, k, target - num, dp, MOD)
            res %= MOD

        dp[n][target] = res
        return res