from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return False

        stack = []
        third = float('-inf')

        for x in reversed(nums):
            if x < third:
                return True
            
            while stack and x > stack[-1]:
                third = max(third, stack.pop())

            stack.append(x)

        return False

