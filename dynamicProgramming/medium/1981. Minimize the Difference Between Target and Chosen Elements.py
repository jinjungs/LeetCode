from typing import List


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        # 현재까지 만들 수 있는 합들을 set으로 관리
        possible_sums = {0}

        for row in mat:
            next_sums = set()
            for num in row:
                for prev_sum in possible_sums:
                    next_sums.add(prev_sum + num)
            possible_sums = next_sums

        return min(abs(s-target) for s in possible_sums)
