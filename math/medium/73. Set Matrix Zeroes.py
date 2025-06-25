from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        x = set()
        y = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    x.add(i)
                    y.add(j)

        for i in x:
            for j in range(n):
                matrix[i][j] = 0

        for j in y:
            for i in range(m):
                matrix[i][j] = 0

# O(1) memory
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

        # Step 1: mark zeros on first row and column
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 2: zero out cells based on marks
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 3: zero out first row if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Step 4: zero out first column if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0

        

