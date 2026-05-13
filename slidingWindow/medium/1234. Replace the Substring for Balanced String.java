class Solution {
    char[] alphas = new char[] {'Q', 'W', 'E', 'R'};

    public int balancedString(String s) {
        int n = s.length();

        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
        }

        int target = n / 4;

        // early return
        if (isBalanced(map, target)) return 0;

        int res = n;
        int l = 0;

        for (int r = 0; r < n; r++) {
            map.put(s.charAt(r), map.get(s.charAt(r)) - 1);

            while (l <= r && isBalanced(map, target)) {
                res = Math.min(res, r - l + 1);
                map.put(s.charAt(l), map.get(s.charAt(l)) + 1);
                l++;
            }
        }

        return res;
    }

    private boolean isBalanced(Map<Character, Integer> map, int target) {
        for (char c : alphas) {
            if (map.getOrDefault(c, 0) > target) return false;
        }
        return true;
    }
}