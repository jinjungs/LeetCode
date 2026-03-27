class Solution {
    List<List<Integer>> res = new ArrayList<>();
    int[] nums; 

    public List<List<Integer>> findSubsequences(int[] nums) {
        this.nums = nums;
        backTrack(0, new ArrayList<>());
        return res;
    }

    public void backTrack(int idx, List<Integer> path) {
        if (path.size() >= 2) {
            res.add(new ArrayList<>(path));
        }

        Set<Integer> used = new HashSet<>();

        for (int i = idx; i < nums.length; i++) {
            if (used.contains(nums[i])) continue;
            if (!path.isEmpty() && path.get(path.size() - 1) > nums[i]) continue;
            used.add(nums[i]);

            path.add(nums[i]);
            backTrack(i+1, path);
            path.remove(path.size()-1);
        }
        
    }
}