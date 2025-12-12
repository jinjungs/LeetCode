class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # two pointer / sliding window
        vowels = set('aeiou')
        n = len(word)
        res = 0

        for left in range(n):
            vowel_count = {}
            consonent_count = 0

            for right in range(left, n):
                char = word[right]

                if char in vowels:
                    vowel_count[char] = vowel_count.get(char, 0) + 1
                else:
                    consonent_count += 1

                if len(vowel_count) == 5 and consonent_count == k:
                    res += 1

                elif consonent_count > k:
                    break

        return res
