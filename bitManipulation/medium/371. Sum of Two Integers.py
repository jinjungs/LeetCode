class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        # a: sum b: carry
        # keep adding carry to sum
        while b != 0:
            tmp = (a & b) << 1
            a = (a ^ b) & mask
            b = tmp & mask

        return a if a <= max_int else ~(a^mask)