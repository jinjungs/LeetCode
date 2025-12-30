from collections import Counter
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        if n < m:
            return 0

        need = Counter(word2)
        have = Counter()
        
        missing = m
        r = 0
        res = 0

        for l in range(n):
            # expand r
            while r < n and missing > 0:
                ch = word1[r]
                have[ch] += 1
                if ch in need and have[ch] <= need[ch]:
                    missing -= 1
                r += 1
            
            if missing == 0:
                res += (n - r + 1)

            # move left boundary
            left_ch = word1[l]
            if left_ch in need and have[left_ch] <= need[left_ch]:
                missing += 1
            have[left_ch] -= 1
            if have[left_ch] == 0:
                del have[left_ch]

        return res
