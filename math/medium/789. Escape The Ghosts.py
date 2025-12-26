from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        tx, ty = target
        dist = abs(tx) + abs(ty)

        for x, y in ghosts:
            if abs(tx-x) + abs(ty-y) <= dist:
                return False

        return True
