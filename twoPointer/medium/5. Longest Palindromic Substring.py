class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(start: int, end: int) -> str:
            if end == len(s) or s[start] != s[end]:
                return s[start]

            result = s[start:end+1]
            j = 1

            while start-j >= 0 and end+j < len(s):
                if s[start-j] != s[end+j]:
                    break
                result = s[start-j] + result + s[end+j]
                j += 1

            return result

        if not s or len(s) == 0:
            return ''

        result = ''
        for i in range(len(s)):
            p1 = palindrome(i, i)
            p2 = palindrome(i, i+1)
            p = p1 if len(p1) > len(p2) else p2
            if len(result) < len(p):
                result = p

        return result
    
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0

        for i in range(len(s)):
            # odd 
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1

            # even
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1

        return res
