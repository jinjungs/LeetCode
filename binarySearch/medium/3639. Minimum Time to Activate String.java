class Solution {
    public int minTime(String s, int[] order, int k) {
        int n = s.length();
        long total = (long) n * (n+1) / 2;

        // edge case
        if (total < k) return -1;

        int l = 0, r = n - 1;
        int time = -1;

        while (l <= r) {
            int t = l + (r -l) / 2;

            // slice order and sorting
            int[] removed = Arrays.copyOfRange(order, 0, t+1);
            Arrays.sort(removed);

            long intact = 0;
            int prev = -1;

            for (int idx: removed) {
                int len = idx - prev - 1;
                intact += (long) len * (len + 1) / 2;
                prev = idx;
            }

            int len = n - prev - 1;
            intact += (long) len * (len + 1) / 2;

            long damaged = total - intact;

            if (damaged >= k) {
                time = t;
                r = t - 1;
            } else {
                l = t + 1;
            }
        }

        return time;
    }
}