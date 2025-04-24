from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 1. count: O(n)
        # d = defaultdict(int)
        # for num in nums:
        #     d[num] += 1
        #     if d.get(num) > 1:
        #         return True
        # return False

        # 2. hash set: O(n)
        # s = set()
        # for num in nums:
        #     if num in s:
        #         return True
        #     s.add(num)
        # return False

        # 3. hash set length: O(n)
        return len(set(nums)) < len(nums)