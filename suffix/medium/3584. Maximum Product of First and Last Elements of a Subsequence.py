from typing import List


class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        n = len(nums)
        INF = float('inf')

        maxArr = [-INF] * n # maxArr[i] : max number from i~ n-1
        minArr = [INF] * n # minArr[i] : min number from i ~ n-1
        maxArr[-1] = minArr[-1] = nums[-1]

        # fill maxArr, minArr
        for i in range(n-2,-1,-1):
            maxArr[i] = max(nums[i], maxArr[i+1])
            minArr[i] = min(nums[i], minArr[i+1])

        res = -INF
        for l in range(n - m +1):
            r = l + m - 1
            res = max(res, nums[l] * maxArr[r], nums[l] * minArr[r])

        return res

        