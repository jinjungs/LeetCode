class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x

        m = abs(n)
        result = 1.0
        current = x

        while m > 0:
            if m % 2 == 1:
                result *= current
            current *= current
            m //= 2

        return result if n > 0 else 1/result

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x = 3 n = 2^31
        # x^2^30 * x^2^30

        def dfs(k:int) -> int:
            if k == 0:
                return 1
            half = dfs(k // 2)
            return half * half * (1 if k % 2 == 0 else x)
            
        res = dfs(abs(n))
        return res if n > 0 else 1 / res        