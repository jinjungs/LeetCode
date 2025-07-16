from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        window = {}
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float('inf')

        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in countT and countT[s[r]] == window[s[r]]:
                have += 1
            
            # shrink
            while need == have:
                if (r-l+1) < resLen:
                    res, resLen = [l,r], r-l+1
                window[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ''
