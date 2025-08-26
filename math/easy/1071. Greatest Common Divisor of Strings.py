import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_len = math.gcd(len(str1), len(str2))
        max_i = -1

        for i in range(gcd_len):
            if str1[i] != str2[i]:
                break
            max_i = i

        if max_i == -1:
            return ''

        # check if it is divided
        gcd = str1[:max_i+1]
        l = len(gcd)
        for j in range(0, len(str1), l):
            if str1[j:j+l] != gcd:
                return ''

        for j in range(0, len(str2), l):
            if str2[j:j+l] != gcd:
                return ''

        return gcd
    

# simple solution
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        g = math.gcd(len(str1), len(str2))
        return str1[:g]