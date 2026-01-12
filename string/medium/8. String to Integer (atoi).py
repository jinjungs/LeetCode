class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        idx = 0
        n = len(s)

        # Whitespace
        while idx < n and s[idx] == ' ':
            idx += 1

        if idx >= n:
            return 0

        # Signedness
        if s[idx] == '+':
            idx += 1
        elif s[idx] == '-':
            sign = -1
            idx += 1
        
        if idx >= n:
            return 0
        
        # Conversion
        # leading zero
        l = idx
        while l < n and s[l] == '0':
            l += 1

        if l >= n or not s[l].isnumeric():
            return 0
        
        r = l
        while r < n and s[r].isnumeric():
            r += 1
        
        # Rounding
        MAX_NUM = 2**31 - 1 if sign > 0 else 2**31
        MAX_NUM_STR = str(MAX_NUM)

        if len(MAX_NUM_STR) < (r-l) or (len(MAX_NUM_STR) == (r-l) and MAX_NUM_STR < s[l:r]):
            return sign * MAX_NUM
        
        return sign * int(s[l:r])
