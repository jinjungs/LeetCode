class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * (n + 1)  # dp[i]: from index i to end, number of ways

        def dfs(i) -> int:
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            if dp[i] != -1:
                return dp[i]                

            res = dfs(i+1)
            if i < n-1 and 10 <= int(s[i:i+2]) <= 26:
                res += dfs(i+2)
            
            dp[i] = res
            return dp[i]

        return dfs(0)
                            