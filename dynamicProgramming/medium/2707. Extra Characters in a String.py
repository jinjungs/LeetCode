from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # dp?
        n = len(s)
        dp = [100] * (n+1) # s[i:] minimun number of extra characters
        dp[n] = 0
        d = set(dictionary)

        # start
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                word = s[i:j+1]
                dp[i] = min(dp[i], (0 if word in d else j-i+1) + dp[j+1])

        return dp[0]
