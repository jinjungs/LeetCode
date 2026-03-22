class Solution {
    public long continuousSubarrays(int[] nums) {
        TreeMap<Integer, Integer> freq = new TreeMap<>();
        int l = 0;
        long res = 0;

        for (int r = 0; r < nums.length; r++) {
            freq.put(nums[r], freq.getOrDefault(nums[r], 0) + 1);

            while (freq.lastKey() - freq.firstKey() > 2) {
                freq.put(nums[l], freq.get(nums[l]) - 1);
                if (freq.get(nums[l]) == 0) {
                    freq.remove(nums[l]);
                }
                l++;
            }

            res += (r - l + 1);
        }

        return res;
    }
}

class Solution {
    public long continuousSubarrays(int[] nums) {
        Deque<Integer> maxD = new ArrayDeque<>();
        Deque<Integer> minD = new ArrayDeque<>();
        
        int l = 0;
        long res = 0;

        for (int r = 0; r < nums.length; r++) {
            while (!maxD.isEmpty() && nums[maxD.peekLast()] < nums[r]) {
                maxD.pollLast();
            }
            maxD.offerLast(r);

            while (!minD.isEmpty() && nums[minD.peekLast()] > nums[r]) {
                minD.pollLast();
            }
            minD.offerLast(r);

            while (nums[maxD.peekFirst()] - nums[minD.peekFirst()] > 2) {
                if (maxD.peekFirst() == l) {
                    maxD.pollFirst();
                }
                if (minD.peekFirst() == l) {
                    minD.pollFirst();
                }
                l++;
            }

            res += (r - l + 1);
        }

        return res;
    }
}