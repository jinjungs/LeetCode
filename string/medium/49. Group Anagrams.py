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

        # 1. Sorting: O(n*mlog(m))
        d = defaultdict(list)
        for s in strs:
            t = str(sorted(s))
            d[t].append(s)

        return list(d.values())
    

        # 2. Hash Table: O(n*m*26)
        for s in strs: # O(n)
            count = [0] * 26 # the key will be the count list of alphabet [0,1,2,...] -> bcc
            for c in s: # O(m)
                count[ord(c) - ord('a')] += 1
            h[tuple(count)].append(s) # list cannot be key 
        return list(h.values())