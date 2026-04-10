class Solution {
    public int rangeSum(int[] nums, int n, int left, int right) {
        // combination        
        List<Integer> comb = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int prev = 0;
            for (int j = i; j < n; j++) {
                prev += nums[j];
                comb.add(prev);
            }    
        }

        Collections.sort(comb);

        int res = 0;
        int m = (int)1e9 + 7;
        for (int i = left - 1; i < right; i++) {
            res = (res + comb.get(i)) % m;
        }

        return res;
    }
}