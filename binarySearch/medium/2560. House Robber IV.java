class Solution {
    public int minCapability(int[] nums, int k) {
        int n = nums.length;

        // max num
        int maxNum = 0;
        for (int num : nums) {
            maxNum = Math.max(maxNum, num);
        }

        // binary search
        int l = 1;
        int r = maxNum;

        while (l <= r) {
            int capacity = l + (r - l) / 2;

            // count house <= capacity
            int prevPrev = 0;
            int prev = 0;
            for (int num : nums) {
                int curr = prev;
                if (num <= capacity) {
                    curr = Math.max(prevPrev + 1, prev);
                }
                prevPrev = prev;
                prev = curr;
            }

            int count = Math.max(prevPrev, prev);

            if (count >= k) {
                r = capacity - 1;
            } else {
                l = capacity + 1;
            }
        }

        return l;

    }
}
