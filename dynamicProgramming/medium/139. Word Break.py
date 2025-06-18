# STA: Should Try Again!!
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)  # Convert list to set for faster lookup
        memo = {}

        def recursive(si: int) -> bool:
            if si == len(s):  # If we reach the end of the string, return True
                return True
            if si in memo:  # If we've already solved this subproblem, return the result
                return memo[si]

            for ei in range(si + 1, len(s) + 1):
                if s[si:ei] in word_set and recursive(ei):
                    memo[si] = True
                    return True

            memo[si] = False
            return False

        return recursive(0)
    
# 25/06/18
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True

        for i in range(n-1, -1, -1):
            for w in wordDict:
                if len(w) <= n - i and w == s[i:i+len(w)]:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]