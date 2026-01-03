from typing import List
from math import lcm

class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d
        r1, r2 = r
        L = lcm(r1, r2)

        def can(T: int) -> bool:
            m1 = T // r1          # drone1 recharge hours
            m2 = T // r2          # drone2 recharge hours
            m12 = T // L          # both recharge hours

            only1 = m2 - m12
            only2 = m1 - m12
            both = T - m1 - m2 + m12

            need1 = d1 - min(d1, only1)
            need2 = d2 - min(d2, only2)

            return need1 + need2 <= both

        # Upper bound: in worst case, at least half of hours are usable (r_i >= 2),
        # so 2*(d1+d2) is safe; add a small buffer.
        lo, hi = 1, 2 * (d1 + d2) + 5

        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo