from typing import List


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        half = n // 2

        s1 = set(nums1)
        s2 = set(nums2)
        
        both = s1 & s2
        only1 = s1 - both
        only2 = s2 - both

        unique1 = min(len(only1), half)
        unique2 = min(len(only2), half)

        total = unique1 + unique2 + len(both) 

        return min(n, total)
