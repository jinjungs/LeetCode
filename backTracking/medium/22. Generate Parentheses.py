from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        len_p = n * 2
        def dfs(k:int, s: str):
            if len(s) == len_p:
                res.append(s)
                return
            if k < n:
                s1 = s + '('
                dfs(k+1, s1)
            if k > len(s) - k:
                s2 = s + ')'
                dfs(k, s2)
        dfs(0, '')
        return res
