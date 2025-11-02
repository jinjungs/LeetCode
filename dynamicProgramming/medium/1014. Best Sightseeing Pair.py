from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        n = len(values)

        dp1 = [0] * n
        dp1[0] = values[0]
        for i in range(1, n):
            dp1[i] = max(dp1[i-1], values[i]+i)


        dp2 = [0] * n
        dp2[n-1] = values[n-1] - n + 1
        for j in range(n-2, -1, -1):
            dp2[j] = max(dp2[j+1], values[j]-j)

        # k is the divider
        # dp1[k] + dp2[k+1]
        res = 0
        for k in range(n-1):
            res = max(res, dp1[k]+dp2[k+1])

        return res
        