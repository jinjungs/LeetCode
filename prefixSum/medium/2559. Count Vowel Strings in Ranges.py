from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = {'a', 'e', 'i', 'o', 'u'}

        # prefixSum[i+1] = sum of words start and end with the vowel, from 0 to i 
        n = len(words)
        prefixSum = [0] * (n+1)

        for i in range(n):
            prefixSum[i+1] = prefixSum[i] + (words[i][0] in vowel and words[i][-1] in vowel)

        return [prefixSum[r+1] - prefixSum[l] for l, r in queries]
