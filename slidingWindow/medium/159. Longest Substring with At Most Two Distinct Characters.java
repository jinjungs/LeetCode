public int longestSubstrings(String s, int k) {
    Map<Character, Integer> map = new HashMap<>();

    int n = s.length();
    int l = 0;
    int res = 0;

    for (int r = 0; r < n; r++) {
        char rc = s.charAt(r);
        map.put(rc, map.getOrDefault(rc, 0) + 1);

        while (map.size() > k) {
            char lc = s.charAt(l);
            map.put(lc, map.get(lc) - 1);

            if (map.get(lc) == 0) {
                map.remove(lc);
            }

            l++;
        }

        res = Math.max(res, r - l + 1);
    }

    return res;
}