class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        int n = nums.length;
        if (n < 2) return false;

        Set<Integer> seen = new HashSet<>();
        int prev = 0;
        int curr = nums[0] % k;
        
        for (int i = 1; i < n; i++) {
            seen.add(prev);
            int newCurr = (curr + nums[i]) % k;
            if (seen.contains(newCurr)) {
                return true;
            }
            prev = curr;
            curr = newCurr;
        }

        return false;
    }
}