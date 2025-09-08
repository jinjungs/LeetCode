from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            m = (l+r) // 2
            # count days
            d, total = 1, 0
            for weight in weights:
                if total + weight <= m:
                    total += weight
                else:
                    total = weight
                    d += 1
                    if d > days:
                        break

            if d > days:
                l = m + 1
            else:
                res = m
                r = m - 1

        return res
