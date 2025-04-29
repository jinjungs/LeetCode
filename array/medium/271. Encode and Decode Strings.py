from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        result = ''
        for s in strs:
            enc = str(len(s)) + '#' + s
            result += enc
        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        if not s:
            return []

        i = 0
        result = []
        while i < len(s):
            j = i+1
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            dec = s[j+1:j+1+length]
            result.append(dec)

            i = j+length+1

        return result
