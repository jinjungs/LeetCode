from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        q = []  # 각 행에 퀸의 위치를 저장 (열 번호만 저장)

        def dfs(row):
            if row == n:
                board = []
                for i in range(n):
                    row_str = ['.'] * n
                    row_str[q[i]] = 'Q'
                    board.append(''.join(row_str))
                res.append(board)
                return

            for col in range(n):
                is_valid = True
                for r in range(row):
                    c = q[r]
                    if c == col or abs(row - r) == abs(col - c):
                        is_valid = False
                        break

                if is_valid:
                    q.append(col)
                    dfs(row + 1)
                    q.pop()

        dfs(0)
        return res
