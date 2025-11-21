

from collections import Counter
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 != 0:
            return []

        c = Counter(changed)
        original = []
        changed.sort()

        for i in range(n):
            key = changed[i]
            if c[key] == 0:
                continue

            twice_key = 2 * key
            if twice_key not in c or c[twice_key] == 0 or c[key] > c[twice_key]:
                return []
            
            original.append(key)
            c[twice_key] -= 1
            c[key] -=1

        return original
                