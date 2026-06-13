class Solution {
    public int longestRepeatingSubstring(String s) {
        int n = s.length();
        int res = 0;

        int l = 1;
        int r = n - 1;

        while (l <= r) {
            int len = l + (r - l) / 2;

            if (appearTwice(s, len)) {
                res = len;
                l = len + 1;
            } else {
                r = len - 1;
            }
        }

        return res;
    }

    private boolean appearTwice(String s, int len) {
        Set<String> seen = new HashSet<>();
        int n = s.length();

        for (int i = 0; i + len <= n; i++) {
            String sub = s.substring(i, i + len);

            if (seen.contains(sub)) {
                return true;
            }

            seen.add(sub);
        }

        return false;
    }
}