class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        l = []
        for i in range(1, n+1):
            if n % i == 0:  
                l.append(i)
                k -= 1
                if k == 0:
                    return i

        return -1