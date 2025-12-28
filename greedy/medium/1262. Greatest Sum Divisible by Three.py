from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # greedy
        total = sum(nums)

        if total % 3 == 0:
            return total

        rest = [[] for _ in range(3)]
        for num in nums:
            rest[num % 3].append(num)
        
        rest[1].sort()
        rest[2].sort()
        
        one = rest[1]
        two = rest[2]

        # 2 가 남을 때
        # (1) 나머지가 2인거 1개 빼
        # (2) 나머지가 1인거 2개 빼
        # (3) 없으면 0

        # 1 이 남을 때
        # (1) 나머지가 1인거 1개 빼
        # (2) 나머지가 2인거 2개 빼

        if total % 3 == 2:
            if len(two) < 1 and len(one) < 2:
                return 0
            if len(one) < 2:
                return total - two[0]
            if len(two) < 1:
                return total - (one[0]+one[1])
            return total - min(two[0], one[0]+one[1])
        else:
            if len(one) < 1 and len(two) < 2:
                return 0
            if len(two) < 2:
                return total - one[0]
            if len(one) < 1:
                return total - (two[0]+two[1])
            return total - min(one[0], two[0]+two[1])

 