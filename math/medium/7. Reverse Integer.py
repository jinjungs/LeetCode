class Solution:
    def reverse(self, x: int) -> int:
        MIN_VAL = -2**31
        MAX_VAL = 2**31 - 1
        
        res = 0
        sign = 1 if x > 0 else -1
        x = abs(x)

        while x != 0:
            pop = x % 10
            x //= 10
            
            # Check for overflow BEFORE multiplying
            if res > (MAX_VAL - pop) // 10:
                return 0

            res = res * 10 + pop

        return res * sign