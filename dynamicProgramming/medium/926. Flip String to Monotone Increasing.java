class Solution {
    public int minFlipsMonoIncr(String s) {
        int n = s.length();
        int[] dp = new int[n];

        int one = s.charAt(0) - '0';

        for (int i = 1; i < n; i++) {
            char c = s.charAt(i);
            if (c == '1') {
                dp[i] = dp[i-1];
                one++;
            } else {
                // change all 1 to 0 or change itself to 1
                dp[i] = Math.min(one, dp[i-1] + 1);
            }
        }

        return dp[n-1];
    }
}