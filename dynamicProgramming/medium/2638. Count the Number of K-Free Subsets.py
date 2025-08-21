from collections import defaultdict
from typing import List
class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        buckets = defaultdict(list)
        for v in nums:
            buckets[v % k].append(v)
        print(buckets)

        def ways_for_bucket(values: List[int]) -> int:
            values.sort()
            total = 1

            # split into +k chains
            i, n = 0, len(values)
            while i < n:
                j = i
                # extend j to end of this +k chain
                # if next value is exactly "k" away, put in the same chain
                while j + 1 < n and values[j+1] == values[j] + k:
                    j += 1

                # House Robber DP
                # dp0: ways up to prev (skip prev)
                # dp1: ways up to prev (take prev)
                dp0, dp1 = 1, 0 
                for _ in range(i, j+1):
                    new_dp0 = dp0 + dp1 # skip current
                    new_dp1 = dp0       # take current
                    dp0, dp1 = new_dp0, new_dp1

                total *= (dp0 + dp1)
                i = j + 1

            return total

        res = 1
        for vals in buckets.values():
            res *= ways_for_bucket(vals)
        return res