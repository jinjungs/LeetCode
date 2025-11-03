from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """
        1, 2, 3
        4, 5, 6
        7, 8, 9

        answer[i][j] = i-k ~ i+k, j-k ~ j+k
        answer[i][j] = dp[i+k][j+k] - dp[i-k-1][j-1] - dp[i-1][j-k-1] + dp[i-k-1][j-k-1]
        """

        ROWS, COLS = len(mat), len(mat[0])
        prefix_sum = [[0] * (COLS+1) for _ in range(ROWS+1)]

        # prefix_sum[i][j] = (0,0) ~ (i-1,j-1)
        for i in range(1, ROWS+1):
            for j in range(1, COLS+1):    
                prefix_sum[i][j] = prefix_sum[i][j-1] + prefix_sum[i-1][j] - prefix_sum[i-1][j-1] + mat[i-1][j-1]

        answer = [[0] * COLS for _ in range(ROWS)]
        for i in range(1, ROWS+1):
            for j in range(1, COLS+1):
                si, sj = max(0, i-k-1), max(0, j-k-1)
                li, lj = min(i+k, ROWS), min(j+k, COLS)
                answer[i-1][j-1] = prefix_sum[li][lj] - prefix_sum[li][sj] - prefix_sum[si][lj] + prefix_sum[si][sj]

        return answer
    