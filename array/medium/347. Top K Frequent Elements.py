from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Sorting: O(nlogn)
        # count the number of occurance in hashmap
        # d = defaultdict(int)
        # for num in nums:
        #     d[num] += 1
        
        # # how to return k most frequent element?
        # rest = k
        # result = []
        # for key, value in sorted(d.items(), key=lambda item: item[1], reverse=True):
        #     result.append(key)
        #     rest -=1
        #     if rest <=0:
        #         break

        # return result

        # 2. Bucket Sort
        count = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] += 1
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq)- 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res