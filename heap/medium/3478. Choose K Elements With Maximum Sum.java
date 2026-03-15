// fist solution
class Solution {
    public long[] findMaxSum(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;

        Map<Integer, PriorityQueue<Integer>> map = new HashMap<>();
        int maxVal = 0;

        for (int i = 0; i < n; i++) {
            int val = nums1[i];
            maxVal = Math.max(maxVal, val);

            map.putIfAbsent(val, new PriorityQueue<>());
            PriorityQueue<Integer> pq = map.get(val);

            pq.offer(nums2[i]);
            if (pq.size() > k) pq.poll();
        }

        long[] prefix = new long[maxVal+1];
        PriorityQueue<Integer> prev = new PriorityQueue<>();
        long sum = 0;

        for (int i = 1; i < maxVal + 1; i++) {
            PriorityQueue<Integer> pq = map.get(i-1);
            if (pq != null) {
                while (!pq.isEmpty()) {
                    int num = pq.poll();
                    prev.offer(num);
                    sum += num;
                    if (prev.size() > k) {
                        int remove = prev.poll();
                        sum -= remove;
                    }
                }
            }
            
            prefix[i] = sum;
        }

        long[] res = new long[n];
        for (int i = 0; i < n; i++) {
            res[i] = prefix[nums1[i]];
        }

        return res;
    }
}

// Sweep line + heap pattern
class Solution {
    public long[] findMaxSum(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;
        long[] res = new long[n];

        int[][] arr = new int[n][3];
        for (int i = 0; i < n; i++) {
            arr[i][0] = nums1[i];
            arr[i][1] = nums2[i];
            arr[i][2] = i;
        }

        Arrays.sort(arr, (a, b) -> Integer.compare(a[0], b[0]));

        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        long sum = 0;
        int i = 0;

        while (i < n) {
            int j = i;
            int currVal = arr[i][0];

            // 1. Same nums1 value gets the current sum first
            while (j < n && arr[j][0] == currVal) {
                res[arr[j][2]] = sum;
                j++;
            }

            // 2. Then add this group's nums2 into heap
            for (int p = i; p < j; p++) {
                minHeap.offer(arr[p][1]);
                sum += arr[p][1];

                if (minHeap.size() > k) {
                    sum -= minHeap.poll();
                }
            }

            i = j;
        }

        return res;
    }
}