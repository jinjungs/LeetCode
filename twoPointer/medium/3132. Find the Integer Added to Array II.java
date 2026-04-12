class Solution {
    public int minimumAddedInteger(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);

        int x1 = nums2[0] - nums1[0];
        int x2 = nums2[0] - nums1[1];
        int x3 = nums2[0] - nums1[2];

        int[] xArr = new int[]{x1, x2, x3};

        int res = Integer.MAX_VALUE;

        for (int x : xArr) {
            int i = 0;
            int j = 0;
            int skip = 0;
            while (i < nums1.length && j < nums2.length) {
                if (nums1[i] + x == nums2[j]) {
                    i++;
                    j++;
                } else {
                    i++;
                    skip++;
                }
            }
            
            // Remaining nums1 elements are also skipped
            skip += nums1.length - i;

            if (j == nums2.length && skip == 2) {
                res = Math.min(res, x);
            }
        }

        return res;
    }
}