from collections import defaultdict
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        s = 0
        res = 0
        for v in nums:
            s += (v & 1)
            res += cnt[s - k]
            cnt[s] += 1
        return res