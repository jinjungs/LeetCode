class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for length in range(1, n+1): # length of word
            for l in range(n - length + 1):
                r = l + length - 1
                if l == r:
                    dp[l][r] = 1
                elif s[l] == s[r]:
                    dp[l][r] = 2 + (dp[l + 1][r - 1] if l + 1 <= r - 1 else 0)
                else:
                    dp[l][r] = max(dp[l+1][r], dp[l][r-1])

        return dp[0][n-1]

   