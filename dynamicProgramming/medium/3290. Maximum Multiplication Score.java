class Solution {
    public long maxScore(int[] a, int[] b) {
        int n = b.length;
        
        // dp[i][j]: i in b, consider j number of indices
        final long NEG_INF = (long) -4e18;

        long[][] dp = new long[n+1][5];
        
        // Initialize
        for (int i = 0; i <= n; i++) {
            Arrays.fill(dp[i], NEG_INF);
            dp[i][0] = 0; // picking 0 items is always 0
        }
        dp[0][0] = 0;

        for (int i = 1; i < n+1; i++) {
            for (int j = 1; j <= 4; j++) {
                if (j > i) break;

                // Option 1: do not use b[i-1]
                dp[i][j] = dp[i - 1][j];

                // Option 2: use b[i-1] as the j-th pick
                if (dp[i - 1][j - 1] != NEG_INF) {
                    long gain = (long) b[i - 1] * (long) a[j - 1];
                    dp[i][j] = Math.max(dp[i][j], dp[i - 1][j - 1] + gain);
                }

                // prev code problem: not possible route is always 0, and participates in the calculation, which is not intended.
                // dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-1] + b[i-1] * a[j-1]);
            }
        }

        return dp[n][4];
    }
}