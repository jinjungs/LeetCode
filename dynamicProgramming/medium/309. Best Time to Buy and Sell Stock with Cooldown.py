from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # hold, sold, rest
        dp = [[0,0,0] for _ in range(n)]
        dp[0][0] = -prices[0]

        for i in range(1, n):
            # 오늘 hold하려면 
            # 1) 전날 hold, 오늘 아무것도 하지 않음
            # 2) 전날 rest, 오늘 매수
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])

            # 오늘 sold하려면 전날 hold
            dp[i][1]= dp[i-1][0] + prices[i]

            # 오늘 rest하려면
            # 1) 전날 sold
            # 2) 전날 rest
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])

        return max(dp[-1])