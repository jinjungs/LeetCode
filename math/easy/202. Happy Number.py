class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            next_n = 0
            while n > 0:
                next_n += (n % 10)**2
                n //= 10
            n = next_n

        return False