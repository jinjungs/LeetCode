from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix & Suffix
        n = len(nums)
        prefix = [0] * n #[1,2,4,6]
        postfix = [0] * n # [48,24,6,1]
        result = [0] * n

        prefix[0] = postfix[n-1] = 1

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for j in range(n-2, -1, -1):
            postfix[j] = postfix[j+1] * nums[j+1]
        for i in range(n):
            result[i] = prefix[i] * postfix[i]
        return result