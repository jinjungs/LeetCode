class Solution {
    public int countSubmatrices(int[][] grid, int k) {
        if (grid[0][0] > k) return 0;

        int ROWS = grid.length;
        int COLS = grid[0].length;

        // sum[i][j] = sum from 0,0 to i-1, j-1
        int[][] sum = new int[ROWS+1][COLS+1];
        int count = 0;
        
        for (int r = 1; r <= ROWS; r++) {
            for (int c = 1; c <= COLS; c++) {
                sum[r][c] = sum[r-1][c] + sum[r][c-1] + grid[r-1][c-1] - sum[r-1][c-1];
                if (sum[r][c] <= k) count++;
            }
        }

        return count;
    }
}