class Solution {
    String s;

    public List<String> ambiguousCoordinates(String s) {
        this.s = s.substring(1, s.length() - 1);
        int n = this.s.length();

        List<String> res = new ArrayList<>();
        for (int i = 1; i < n; i++) {
            List<String> l = makeCombination(0, i-1);
            List<String> r = makeCombination(i, n-1);
            for (String s1: l) {
                for (String s2: r) {
                    res.add("(" + s1 + ", " + s2 + ")");
                }
            }
        }

        return res;
    }

    public List<String> makeCombination(int l, int r) {
        List<String> res = new ArrayList<>();
        String sub = s.substring(l, r+1);
        int n = sub.length();
        
        if (n == 1 || sub.charAt(0) != '0') {
            res.add(sub);
        }

        for (int i = 1; i < n; i++) {
            String left = sub.substring(0, i);
            String right = sub.substring(i);

            if (left.length() > 1 && left.charAt(0) == '0') continue;

            if (right.charAt(right.length() - 1) == '0') continue;

            res.add(left + "." + right);
        }

        return res;
    }
}