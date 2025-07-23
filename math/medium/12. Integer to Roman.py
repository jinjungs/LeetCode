class Solution:
    def intToRoman(self, num: int) -> str:
        one = {0: 'I', 1: 'X', 2: 'C', 3: 'M'}
        five = {0: 'V', 1: 'L', 2: 'D', 3: ''}

        def convert(m:int, seat:int) -> str:
            q = m // 5
            r = m % 5
            if m == 4:
                return one[seat] + five[seat] * (q+1)
            elif m == 9:
                return one[seat] + one[seat+1] * q
            else:
                return five[seat] * q + one[seat] * r
                
        res = ''
        num = str(num)
        n = len(num)
        for i in range(n):
            res += convert(int(num[i]), n-1-i)

        return res