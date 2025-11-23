class Solution:
    def minSteps(self, n: int) -> int:
        # n = 5
        # 소수 n
        # 10 = 2 * 5 (sum)
        # copy, paste * (2-1), copy, paste * (5-1) = 7
        # copy, paste * (5-1), copy, paste = 7
        
        # (1) 소인수분해
        res = 0
        for i in range(2, n+1):
            if n < i:
                break
            while n % i == 0:
                res += i
                n //= i
        return res
    
class Solution:
    def minSteps(self, n: int) -> int:
        # (2) DP
        dp = [1001] * (n+1)
        dp[0] = dp[1] = 0

        for i in range(2, n+1):
            for j in range(1, i):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + (i//j))

        return dp[n]
