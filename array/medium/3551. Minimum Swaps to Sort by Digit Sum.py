from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        arr = []

        # 1) (digitSum, value, originalIndex) 만들기
        for i, num in enumerate(nums):
            t = num
            s = 0
            while t > 0:
                s += t % 10
                t //= 10
            arr.append((s, num, i))

        # 2) digitSum 기준 정렬
        arr.sort()

        # 3) 원래 인덱스 -> 정렬 후 인덱스 맵핑 만들기
        pos = [0] * n
        for sorted_idx, (_, _, original_idx) in enumerate(arr):
            pos[original_idx] = sorted_idx

        # 4) 순열 pos 에서 cycle 분해
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or pos[i] == i:
                continue  # 이미 제자리면 건너뜀

            cycle_len = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = pos[j]
                cycle_len += 1

            swaps += cycle_len - 1

        return swaps
        