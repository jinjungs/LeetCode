class Solution {
    public boolean[] isArraySpecial(int[] nums, int[][] queries) {
        int n = nums.length;

        // prefix[i] = number of bad adjacent pairs in nums[0..i-1]
        int[] prefix = new int[n];

        for (int i = 0; i < n - 1; i++) {
            prefix[i + 1] = prefix[i];
            if ((nums[i] % 2) == (nums[i + 1] % 2)) {
                prefix[i + 1]++;
            }
        }

        boolean[] res = new boolean[queries.length];

        for (int i = 0; i < queries.length; i++) {
            int l = queries[i][0];
            int r = queries[i][1];

            // bad pair exists in [l, r-1] ?
            res[i] = (prefix[r] - prefix[l] == 0);
        }

        return res;
    }
}