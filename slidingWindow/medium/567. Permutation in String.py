class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        window_count = [0] * 26
        
        for ch in s1:
            s1_count[ord(ch) - ord('a')] += 1
        
        for i in range(len(s2)):
            window_count[ord(s2[i]) - ord('a')] += 1
            
            #If the window size exceeds the length of s1, remove the leftmost character from the window.
            if i >= len(s1):
                window_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            
            if window_count == s1_count:
                return True
        
        return False