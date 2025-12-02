from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        letter_len = 10
        d = defaultdict(int)
        res = []

        for i in range(n - letter_len + 1):
            dna = s[i:i+letter_len]
            d[dna] += 1
            if d[dna] == 2:
                res.append(dna)

        return res
