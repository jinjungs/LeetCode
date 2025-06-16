class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []
        
        for i in range(len(s)):
            # odd
            l, r  = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res.append(s[l:r+1])
                l -= 1
                r += 1
        
            # even
            l, r  = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res.append(s[l:r+1])
                l -= 1
                r += 1

        return len(res)
