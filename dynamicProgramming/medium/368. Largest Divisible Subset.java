class Solution {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        List<List<Integer>> dp = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            List<Integer> subset = new ArrayList<>();
            for (int j = 0; j < i; j++) {
                if (nums[i] % nums[j] == 0 && dp.get(j).size() > subset.size()) {
                    subset = new ArrayList<>(dp.get(j));
                }
            }           
            subset.add(nums[i]);
            dp.add(subset);
        }

        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (dp.get(i).size() > res.size()){
                res = dp.get(i);
            }
        }

        return res;
    }
}

class Solution {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;

        int[] dp = new int[n];
        int[] prev = new int[n];

        Arrays.fill(dp, 1);
        Arrays.fill(prev, -1);

        int maxLen = 1;
        int lastIdx = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] % nums[j] == 0 && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    prev[i] = j;
                }
            }

            if (dp[i] > maxLen) {
                maxLen = dp[i];
                lastIdx = i;
            }
        }

        List<Integer> res = new ArrayList<>();
        while (lastIdx != -1) {
            res.add(nums[lastIdx]);
            lastIdx = prev[lastIdx];
        }

        Collections.reverse(res);
        return res;
    }
}