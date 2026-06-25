class Solution {
    public int findMaxLength(int[] nums) {
        int zero = 0;
        int one = 0;

        Map<Integer, Integer> diffMap = new HashMap<>();
        diffMap.put(0, 0);

        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (num == 0) {
                zero++;
            } else {
                one++;
            }

            int diff = one - zero;
            if (diffMap.containsKey(diff)) {
                res = Math.max(res, i + 1 - diffMap.get(diff));
            } else {
                diffMap.put(diff, i + 1);
            }
        }

        return res;        

    }
}