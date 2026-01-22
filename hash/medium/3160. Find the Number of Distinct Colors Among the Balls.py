from collections import defaultdict
from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = defaultdict(int) # key: color, value: number of balls which is that color
        marked = {} # key: index, value: color
        res = []

        for x, y in queries:
            if x in marked:
                colors[marked[x]] -= 1
                if colors[marked[x]] == 0:
                    del colors[marked[x]]
            
            marked[x] = y
            colors[y] += 1
            res.append(len(colors))

        return res    