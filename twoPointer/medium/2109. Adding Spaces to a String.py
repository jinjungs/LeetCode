from typing import List

# Set
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        spaces = set(spaces)

        for i in range(len(s)):
            if i in spaces:
                res.append(' ')
            res.append(s[i])

        return ''.join(res)

# Two Pointer
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        space_idx = 0
        res = []

        for i in range(len(s)):
            if space_idx < len(spaces) and i == spaces[space_idx]:
                res.append(' ')
                space_idx += 1
            res.append(s[i])

        return ''.join(res)