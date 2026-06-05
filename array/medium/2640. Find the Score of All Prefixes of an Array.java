class Solution {
    public long[] findPrefixScore(int[] nums) {
        int n = nums.length;
        long[] score = new long[n];
        long max = 0;
        long sum = 0;

        for (int i = 0; i < n; i++) {
            max = Math.max(max, nums[i]);
            sum += nums[i] + max;
            score[i] = sum;
        }

        return score;
    }
}