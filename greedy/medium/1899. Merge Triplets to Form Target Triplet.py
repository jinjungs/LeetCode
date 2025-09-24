from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target
        first = second = third = False

        for na, nb, nc in triplets:
            if na > a or nb > b or nc > c:
                continue
            if na == a:
                first = True
            if nb == b:
                second = True
            if nc == c:
                third = True

        return first and second and third
            