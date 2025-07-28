from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        for i in range(1 << n):  # 0 ~ 2^n - 1
            res.append(i ^ (i >> 1))
        return res