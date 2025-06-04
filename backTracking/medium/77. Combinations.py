from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 5C3 = (4C2 arr plus 5) + 4C3
        def recursive(n, k):
            if n == k:
                return [[x for x in range(1,n+1)]]
            if k == 1:
                return [[x] for x in range(1,n+1)]

            return [x + [n] for x in recursive(n-1, k-1)] + recursive(n-1, k)

        return recursive(n, k)