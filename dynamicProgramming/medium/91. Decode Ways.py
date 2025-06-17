# Top-Down
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
    
# Bottom-Up
class Solution2:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        
        dp = {len(s): 1} # one way to decode empty strings
        dp[n-1] = 0 if s[n-1] == '0' else 1

        for i in range(n-2, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                one_digit = dp[i + 1]
                two_digit = dp[i + 2] if int(s[i:i+2]) <= 26 else 0
                dp[i] = one_digit + two_digit

        return dp[0]
                            
# Bottom-Up (Space Optimized)
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp1, dp2 = 1, 0

        for i in range(n-1, -1, -1):
            curr = 0
            if s[i] != "0":
                curr += dp1
                if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                    curr += dp2
            dp2 = dp1
            dp1 = curr

        return dp1