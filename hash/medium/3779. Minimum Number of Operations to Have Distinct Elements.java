class Solution {
    public int minOperations(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        int excess = 0;

        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
            if (freq.get(num) > 1) excess++;
        }

        int n = nums.length;
        int oper = 0;
        int i = 0;

        while (excess > 0 && i < n) {
            // remove first three
            for (int j = i; j < Math.min(i + 3, n); j++) {
                if (freq.get(nums[j]) > 1) {
                    excess--;
                }
                freq.put(nums[j], freq.get(nums[j]) - 1);
            }
            oper++;
            i += 3;
        }

        return oper;
    }
}

class Solution2 {
    public int minOperations(int[] nums) {
        int[] hash = new int[100001];
        int i = 0;
        for(i = nums.length - 1; i >= 0; i--) {
            if(hash[nums[i]] == 1) break;
            hash[nums[i]] = 1;
        }
        return (i + 3) / 3;
    }
}