from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remain = [0] * k
        for num in arr:
            remain[num % k] += 1

        if remain[0] % 2 != 0:
            return False
            
        for i in range(1, k//2 + 1):
            if remain[i] != remain[k-i]:
                return False

        return True