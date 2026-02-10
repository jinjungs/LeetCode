from collections import defaultdict
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
    
        max_num = max(nums)

        # dp[i] = i까지 고려했을 때 얻을 수 있는 최대 점수
        dp = [0] * (max_num + 1)
        dp[1] = count[1] * 1

        for i in range(2, max_num + 1):
            dp[i] = max(
                dp[i-1],
                dp[i-2] + i * count[i]
            )

        return dp[max_num]
