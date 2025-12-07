from collections import defaultdict
from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        
        for i, row in enumerate(nums):
            for j, num in enumerate(row):
                diagonals[i + j].append(num)
        
        res = []
        for key in sorted(diagonals.keys()):
            res.extend(diagonals[key][::-1])
        
        return res