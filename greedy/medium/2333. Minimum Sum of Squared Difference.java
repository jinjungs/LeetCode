class Solution {
    public long minSumSquareDiff(int[] nums1, int[] nums2, int k1, int k2) {
        int n = nums1.length;
        long k = (long) k1 + k2;

        int maxD = 0;
        int[] diff = new int[n];
        for (int i = 0; i < n; i++) {
            diff[i] = Math.abs(nums1[i] - nums2[i]);
            maxD = Math.max(maxD, diff[i]);
        }

        long[] cnt = new long[maxD + 1];
        for (int d: diff) cnt[d]++;

        for (int d = maxD; d > 0 && k > 0; d--) {
            if (cnt[d] == 0) continue;

            long move = Math.min(cnt[d], k);
            cnt[d] -= move;
            cnt[d - 1] += move;
            k -= move;

            // 아직 k가 남으면 같은 d에서 또 내려야 하니, 다음 루프에서 계속 처리됨
            // (cnt[d]가 남아있으면 또 move 처리)
            if (cnt[d] > 0 && k > 0) d++;
        }

        long res = 0;
        for (int d = 0; d <= maxD; d++) {
            if (cnt[d] == 0) continue;
            res += cnt[d] * (long) d * d;
        }
        return res;

    }
}