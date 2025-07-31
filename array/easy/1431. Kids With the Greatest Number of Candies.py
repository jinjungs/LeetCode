from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        res = [False] * len(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                res[i] = True

        return res