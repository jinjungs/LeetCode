from typing import List
class Solution:
    def minCost(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)

        # dp[i][j], i: last prefix element, j: starting index
        dp = {}
        dp[nums[0]] = max(nums[1], nums[2])
        dp[nums[1]] = max(nums[0], nums[2])
        dp[nums[2]] = max(nums[0], nums[1])

        i = 3
        while i + 1 < n:
            p, q = nums[i], nums[i+1]
            curr = {}
            
            for x, cost in dp.items():
                nx = x
                add = max(p, q)
                curr[nx] = min(curr.get(nx, float('inf')), cost + add)

                nx = p
                add = max(x, q)
                curr[nx] = min(curr.get(nx, float('inf')), cost + add)

                nx = q
                add = max(x, p)
                curr[nx] = min(curr.get(nx, float('inf')), cost + add)

            dp = curr
            i += 2

        # finialize
        res = float('inf')
        if i == n:
            # only survivor remains
            for x, cost in dp.items():
                res = min(res, cost + x)
        else:
            # one element left in nums: nums[i]
            last = nums[i]
            for x, cost in dp.items():
                res = min(res, cost + max(x, last))

        return res

