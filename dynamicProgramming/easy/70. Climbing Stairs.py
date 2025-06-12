class Solution:
    def climbStairs(self, n: int) -> int:
        """
        n=1 1
        n=2 2
        n=3 3 pick 1 f(2) + pick 2 f(2)
        n=4 5 pick 1 f(3) + pick 2 f(2)
        """
        d = [0] * (n+1)
        d[0] = d[1] = 1

        def recursive(x):
            if d[x] != 0:
                return d[x]
            d[x] = recursive(x-1) + recursive(x-2)
            return recursive(x-1) + recursive(x-2)

        return recursive(n)
    
# 25/06/12
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-1):
            one, two = one + two, one

        return one