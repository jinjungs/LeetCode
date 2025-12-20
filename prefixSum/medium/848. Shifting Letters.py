from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(shifts)
        res = []

        changed_shifts = [0] * n
        prev = 0
        for i in range(n-1, -1, -1):
            changed_shifts[i] = (prev + shifts[i]) % 26
            prev = changed_shifts[i]

        for i in range(n):
            res.append(chr((ord(s[i]) - ord('a') + changed_shifts[i]) % 26 + ord('a')))

        return ''.join(res)
