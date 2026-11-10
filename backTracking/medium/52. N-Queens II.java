class Solution {
    boolean[] visitedCol;
    boolean[] visitedDiag1;
    boolean[] visitedDiag2;
    int res;

    public int totalNQueens(int n) {
        visitedCol = new boolean[n];
        visitedDiag1 = new boolean[2 * n - 1];
        visitedDiag2 = new boolean[2 * n - 1];
        res = 0;

        backTrack(0, n);

        return res;
    }

    private void backTrack(int row, int n) {
        if (row == n) {
            res++;
            return;
        }

        for (int col = 0; col < n; col++) {
            if (visitedCol[col] || visitedDiag1[row - col + n - 1] || visitedDiag2[row + col]) continue;

            visitedCol[col] = true;
            visitedDiag1[row - col + n - 1] = true;
            visitedDiag2[row + col] = true;

            backTrack(row + 1, n);

            visitedDiag2[row + col] = false;
            visitedDiag1[row - col + n - 1] = false;
            visitedCol[col] = false;
        }
    }
}