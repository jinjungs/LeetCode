class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        d[i][j] = d[i-1][j] + d[i][j-1]

        1 1 1 1 1 1 1
        1 2 3 4 5 6 7
        1 3 6 10 15 21 28
        """
        paths = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            paths[i][0] = 1
            for j in range(1, n):
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
        return paths[-1][-1]

# 25/06/19 
# Space Optimized
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1,m):
            for j in range(1,n):
                dp[j] = dp[j-1] + dp[j]

        return dp[n-1]