class Solution {
    int[][] grid;

    public int numMagicSquaresInside(int[][] grid) {
        // count: (10-3+1)^2 = 8*8 = 64
        // in the grid: (3 + 3 + 2) * 3 = 8 * 3 = 24
        // if contains grid[i][j] 10 ~ 15 => invalid

        this.grid = grid;
        
        // Brute Force
        int ROWS = grid.length;
        int COLS = grid[0].length;

        if (ROWS < 3 || COLS < 3) return 0;

        int count = 0;

        for (int r = 0; r <= ROWS - 3; r++) {
            for (int c = 0; c <= COLS - 3; c++) {
                // from grid[r][c] ~ grid[r+2][c+2]
                // Check Element
                if (!checkElement(r, c)) continue;

                // Check ROW, COL
                int rowSum = checkRowColSum(r, c);
                if (rowSum == -1) continue;

                // Check Diagonals
                if (!checkDiagonal(rowSum, r, c)) continue;
                
                count++;
            }
        }

        return count;
    }

    private boolean checkElement(int r, int c) {
        boolean[] visited = new boolean[10];

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                int num = grid[r+i][c+j];
                if (num > 9 || num <= 0) return false;
                if (visited[num]) return false;
                visited[num] = true;
            }
        }
        return true;
    }

    private int checkRowColSum(int r, int c) {
        int prev = -1;

        for (int i = 0; i < 3; i++) {
            int rowSum = grid[r+i][c] + grid[r+i][c+1] + grid[r+i][c+2];
            int colSum = grid[r][c+i] + grid[r+1][c+i] + grid[r+2][c+i];
            
            if (rowSum != colSum) {
                return -1;
            }

            if (prev == -1) {
                prev = rowSum;
                continue;
            }

            if (prev != rowSum) {
                return -1;
            }
        }

        return prev;
    }

    private boolean checkDiagonal(int rowSum, int r, int c) {
        int a = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2];
        int b = grid[r+2][c] + grid[r+1][c+1] + grid[r][c+2];
        return (a == b && b == rowSum);
    }

 
}