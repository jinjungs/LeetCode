class Solution {
    int ROWS; 
    int COLS;
    int[][] grid;

    public int[][] differenceOfDistinctValues(int[][] grid) {
        ROWS = grid.length;
        COLS = grid[0].length;
        this.grid = grid;

        int[][] res = new int[ROWS][COLS];

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                int left = above(r, c, -1);
                int right = above(r, c, 1);
                res[r][c] = Math.abs(left - right);
            }
        }

        return res;
    }

    private int above(int r, int c, int sign) {
        int x = r + sign;
        int y = c + sign;

        Set<Integer> set = new HashSet<>();

        while (0 <= x && x < ROWS && 0 <= y && y < COLS) {
            set.add(grid[x][y]);
            x += sign;
            y += sign;
        }

        return set.size();
    }
}