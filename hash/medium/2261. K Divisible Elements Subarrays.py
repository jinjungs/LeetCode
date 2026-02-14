from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        res = set()

        for l in range(n):
            count = 0
            r = l
            arr = []
            for r in range(l, n):
                if nums[r] % p == 0:
                    count += 1
                if count > k:
                    break

                arr.append(nums[r])
                res.add(tuple(arr))

        return len(res)

        