
class Solution {
    public boolean validPartition(int[] nums) {
        // dp[i]: is valid before i
        int n = nums.length;
        boolean[] dp = new boolean[n+1];
        dp[0] = true;

        for (int i = 1; i < n; i++) {
            if (dp[i-1] && nums[i-1] == nums[i]) {
                dp[i+1] = true;
            } 
            
            if (i > 1 && dp[i-2]) {
                int a = nums[i-2], b = nums[i-1], c = nums[i];
                if ((a == b && b == c) || (a + 1 == b && b + 1 == c)) {
                    dp[i+1] = true;
                } 
            }
        }

        return dp[n];
    }
}