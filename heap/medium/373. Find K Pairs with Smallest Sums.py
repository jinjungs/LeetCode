from heapq import heappush, heappop
from typing import List
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        res = []

        # nums1의 각 원소 + nums2[0]만 먼저 넣기
        for i in range(min(len(nums1), k)):
            heappush(h, (nums1[i] + nums2[0], i, 0))

        while h and len(res) < k:
            _, i, j = heappop(h)
            res.append([nums1[i], nums2[j]])

            # 같은 i에서 다음 후보
            if j + 1 < len(nums2):
                heappush(h, (nums1[i] + nums2[j+1], i, j+1))

        return res
        