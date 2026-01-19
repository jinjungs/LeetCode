class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        
        def best(target: str) -> int:
            res = 0
            l = 0
            flips = 0

            for r in range(n):
                if answerKey[r] != target:
                    flips += 1

                while flips > k:
                    if answerKey[l] != target:
                        flips -= 1
                    l += 1

                res = max(res, r-l+1)
            
            return res

        return max(best('F'), best('T'))
            
