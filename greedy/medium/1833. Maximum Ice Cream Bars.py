from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = len(costs)
        costs.sort()
        rest = coins
        cnt = 0

        for cost in costs:
            if rest < cost:
                break
            rest -= cost
            cnt += 1

        return cnt
