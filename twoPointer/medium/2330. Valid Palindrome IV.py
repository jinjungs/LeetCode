class Solution:
    def makePalindrome(self, s: str) -> bool:
        change = 0
        l, r = 0, len(s)-1

        while l <= r:
            if s[l] != s[r]:
                change += 1
            if change > 2:
                return False
            l += 1
            r -= 1

        return change <= 2