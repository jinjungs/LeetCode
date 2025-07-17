class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
            
        l = list(word)
        vowel = {'a', 'e', 'i', 'o', 'u'}
        cnt_vowel = 0
        cnt_cons = 0
        for char in l:
            if not char.isalnum():
                return False
            if not char.isalpha():
                continue
            if char.lower() in vowel:
                cnt_vowel += 1
            else:
                cnt_cons += 1

        return cnt_vowel >= 1 and cnt_cons >= 1
        