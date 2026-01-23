from collections import defaultdict
from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(cards) == len(set(cards)):
            return -1

        # key: value, val: last index
        res = len(cards)
        h = {}

        for i, card in enumerate(cards):
            if card in h:
                res = min(res, i - h[card] + 1)
            h[card] = i

        return res
