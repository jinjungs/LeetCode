from typing import Counter, List

# my solution
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        c = Counter(s)
        active = set()
        prev = 0
        res = []

        for i, ch in enumerate(s):
            c[ch] -= 1
            if c[ch] > 0:
                active.add(ch)  
            else:
                active.discard(ch)
            
            if not active:
                res.append(i-prev+1)
                prev = i+1

        return res
    
# Two Pointer (Greedy) - Neetcode
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        return res