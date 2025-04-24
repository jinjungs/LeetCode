from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the number of occurance in hashmap
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        # how to return k most frequent element?
        rest = k
        result = []
        for key, value in sorted(d.items(), key=lambda item: item[1], reverse=True):
            result.append(key)
            rest -=1
            if rest <=0:
                break

        return result