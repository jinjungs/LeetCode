class Solution {
    public int longestSubarray(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        if (n == 1) return 1;

        int[] left = new int[n];
        int[] right = new int[n];

        // left[i]: longest non-decreasing subarray ending at i (no replacement)
        left[0] = 1;
        for (int i = 1; i < n; i++) {
            left[i] = 1;
            if (nums[i] >= nums[i - 1]) {
                left[i] = left[i - 1] + 1;
            }
        }

        // right[i]: longest non-decreasing subarray starting at i (no replacement)
        right[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            right[i] = 1;
            if (nums[i] <= nums[i + 1]) {
                right[i] = right[i + 1] + 1;
            }
        }

        int ans = 1;
        for (int i = 0; i < n; i++) {
            ans = Math.max(ans, left[i]); // no replacement case
        }

        // Try replacing nums[i]
        for (int i = 0; i < n; i++) {
            int best = 1;

            // attach left side only
            if (i > 0) best = Math.max(best, left[i - 1] + 1);

            // attach right side only
            if (i < n - 1) best = Math.max(best, right[i + 1] + 1);

            // attach both sides if possible: nums[i-1] <= x <= nums[i+1]
            if (i > 0 && i < n - 1 && nums[i - 1] <= nums[i + 1]) {
                best = Math.max(best, left[i - 1] + 1 + right[i + 1]);
            }

            ans = Math.max(ans, best);
        }

        return ans;
    }
}