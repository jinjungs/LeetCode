class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k <= 1) return 0;

        int l = 0;
        long curr = 1;
        int res = 0;

        for (int r = 0; r < nums.length; r++) {
            curr *= nums[r];

            while (curr >= k) {
                curr /= nums[l++];
            }

            res += (r - l + 1);
        }

        return res;
    }
}