from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        INF = 10**9        
        
        # dp[j]: 현재 위치에서 lane j에 있을 때 최소 점프
        dp = [INF, 1, 0, 1]  # index 0은 dummy

        n = len(obstacles) 
        for i in range(1, n):
            obs = obstacles[i]
            # if obstacle, cannot jump
            if obs != 0:
                dp[obs] = INF

            for j in range(1,4):
                if j != obs:
                    dp[j] = min(dp[j], min(dp[k] + 1 for k in (1,2,3)))

        return min(dp[1:])
                        