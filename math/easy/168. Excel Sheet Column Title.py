class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            m = columnNumber % 26
            res.append(chr(m + ord('A')))
            columnNumber //= 26

        return ''.join(res[::-1])