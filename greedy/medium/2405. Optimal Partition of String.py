class Solution:
    def partitionString(self, s: str) -> int:
        res = 0
        h = set()
        for c in s:
            if c in h:
                res += 1
                h.clear()
            h.add(c)

        return res + 1