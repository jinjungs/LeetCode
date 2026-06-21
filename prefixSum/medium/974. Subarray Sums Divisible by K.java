class Solution {
    public int subarraysDivByK(int[] nums, int k) {
		Map<Integer, Integer> map = new HashMap<>(); // key: remainder, value: count
		map.put(0,1);

		int prefix = 0;
        int res = 0;

        for (int num : nums) {
            prefix += num;

            int remain = prefix % k;
            if (remain < 0) remain += k;

            int count = map.getOrDefault(remain, 0); 
            res += count;
            map.put(remain, count + 1);
        }

        return res;
    }
}