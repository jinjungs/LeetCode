from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        max_count = 0
        count = defaultdict(int)

        for r in range(len(s)):
            count[s[r]] += 1
            max_count = max(max_count, count[s[r]])

            # If replacements needed exceed k, shrink window
            if (r - l + 1) - max_count > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res
