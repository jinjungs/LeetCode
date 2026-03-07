class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        Map<Integer, Long> minPrefix = new HashMap<>();
        
        long prefix = 0;
        long res = Long.MIN_VALUE;
        
        for (int num : nums) {
            long currPrefix = prefix + num;
            
            if (minPrefix.containsKey(num - k)) {
                res = Math.max(res, currPrefix - minPrefix.get(num - k));
            }
            if (minPrefix.containsKey(num + k)) {
                res = Math.max(res, currPrefix - minPrefix.get(num + k));
            }
            
            minPrefix.put(num, Math.min(
                minPrefix.getOrDefault(num, Long.MAX_VALUE),
                prefix
            ));
            
            prefix = currPrefix;
        }
        
        return res == Long.MIN_VALUE ? 0 : res;
    }
}