class Solution {
    public int findMin(int[] nums) {
        int n = nums.length;
        int l = 0;
        int r = n-1;        
        int res = nums[0];

        while (l <= r) {
            int m = l + (r-l) / 2;
            if (nums[m] > nums[r]) {
                l = m + 1;
            } else {
                res = Math.min(res, nums[m]);
                r = m - 1;
            }
        }

        return res;

    }
}