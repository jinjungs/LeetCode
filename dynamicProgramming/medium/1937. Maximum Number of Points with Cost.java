class Solution {
    public long maxPoints(int[][] points) {
        int ROWS = points.length;
        int COLS = points[0].length;

        long[] prev = new long[COLS];

        for (int i = 0; i < ROWS; i++) {
            long[] curr = new long[COLS];
            
            // left to right
            long leftMax = Long.MIN_VALUE;
            for (int j = 0; j < COLS; j++) {
                leftMax = Math.max(leftMax, prev[j] + j);
                curr[j] = points[i][j] + leftMax - j;
            }

            // right to left
            long rightMax = Long.MIN_VALUE;
            for (int j = COLS -1; j >= 0; j--) {
                rightMax = Math.max(rightMax, prev[j] - j);
                curr[j] = Math.max(curr[j], points[i][j] + rightMax + j);
            }

            prev = curr;
        }

        long res = 0;
        for (int j = 0; j < COLS; j++) {
            res = Math.max(res, prev[j]);
        }

        return res;
    }
}