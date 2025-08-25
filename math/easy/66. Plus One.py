from ast import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        carry = 1
        res = []
        for i in range(n-1, -1, -1):
            cal = digits[i] + carry
            res.append(cal % 10)
            carry = cal // 10

        if carry > 0:
            res.append(carry)
        return res[::-1]