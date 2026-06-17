class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        freq.put(0, 1);

        int curr = 0;
        int res = 0;

        for (int num: nums) {
            curr += num;
            res += freq.getOrDefault(curr - k, 0);
            freq.put(curr, freq.getOrDefault(curr, 0) + 1);
        }

        return res;
    }
}