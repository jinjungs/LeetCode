class Solution {
    public boolean partitionArray(int[] nums, int k) {
        int n = nums.length;
        if (n % k != 0) return false;

        int groupCnt = n / k;
        Map<Integer, Integer> freq = new HashMap<>();

        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
            if (freq.get(num) > groupCnt) return false;
        }

        return true;
    }
}