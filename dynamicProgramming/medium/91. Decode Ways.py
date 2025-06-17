class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = ['#'] * n
        eng_char = set([str(x) for x in range(1,27)])

        def dfs(i, prev) -> int:
            if i >= n:
                return 1
            if dp[i] != '#':
                return dp[i]                

            res = 0
            if s[i:i+1] in eng_char:
                res += dfs(i+1, prev)
            if i < n-1 and s[i:i+2] in eng_char:
                res += dfs(i+2, prev)
            
            dp[i] = res * prev
            return dp[i]

        return dfs(0, 1)
                            