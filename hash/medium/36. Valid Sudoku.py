from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):
            row_set = set()
            col_set = set()
            for j in range(n):
                # row
                if board[i][j] != '.':
                    if board[i][j] in row_set:
                        return False
                    else:
                        row_set.add(board[i][j])
                # column
                if board[j][i] != '.':
                    if board[j][i] in col_set:
                        return False
                    else:
                        col_set.add(board[j][i])

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                grid_set = set()
                for i in range(3):
                    for j in range(3):
                        if board[row+i][col+j] != '.':
                            if board[row+i][col+j] in grid_set:
                                return False
                            grid_set.add(board[row+i][col+j])

        return True
        