class Solution {
    String s;
    int n;

    public int almostPalindromic(String s) {
        this.s = s;
        this.n = s.length();

        int res = 0;
        for (int i = 0; i < n; i++) {
            res = Math.max(res, expand(i, i));
            res = Math.max(res, expand(i, i+1));
        }

        return res;
    }

    private int expand(int l, int r) {
        // Step 1: mismatch 날 때까지 expand
        while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) {
            l--;
            r++;
        }
        
        // Step 2-1: 왼쪽 문자 skip (l-1, r)
        int l1 = l - 1, r1 = r;
        while (l1 >= 0 && r1 < n && s.charAt(l1) == s.charAt(r1)) {
            l1--;
            r1++;
        }
        
        // Step 2-2: 오른쪽 문자 skip (l, r+1)
        int l2 = l, r2 = r + 1;
        while (l2 >= 0 && r2 < n && s.charAt(l2) == s.charAt(r2)) {
            l2--;
            r2++;
        }
        
        return Math.min(n, Math.max(r1 - l1 - 1, r2 - l2 - 1));
    }
}