from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]

        """
        should be equal
        # sorted list
        """
        d = defaultdict(list)
        for s in strs:
            t = str(sorted(s))
            d[t].append(s)

        return list(d.values())