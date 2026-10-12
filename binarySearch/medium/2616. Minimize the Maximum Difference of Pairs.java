class Solution {
    public int minimizeMax(int[] nums, int p) {
        // greedy
        Arrays.sort(nums);

        // adjacent
        // diff[i]: diff nums[i], nums[i+1]

        // binaray search
        int l = 0;
        int r = nums[nums.length-1] - nums[0];

        while (l <= r) {
            int diff = l + (r - l) / 2;
            // can make p pairs with diff
            int pairs = 0;
            int i = 0;
            while (i < nums.length - 1) {
                if (nums[i+1] - nums[i] <= diff) {
                    pairs++;
                    i += 2;
                } else {
                    i++;
                }
            }

            if (pairs >= p) {
                r = diff - 1;
            } else {
                l = diff + 1;
            }
            
        }

        return l;
    }
}