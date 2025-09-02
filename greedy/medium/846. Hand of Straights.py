from collections import Counter
from typing import List
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        c = Counter(hand)
        hand.sort()
        
        for num in hand:
            if c[num] == 0:
                continue
            for i in range(groupSize):
                if (num + i) not in c or c[num+i] == 0:
                    return False
                c[num+i] -= 1

        return True
