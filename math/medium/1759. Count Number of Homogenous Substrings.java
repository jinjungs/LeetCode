class Solution {
    public int countHomogenous(String s) {
        int m = 1_000_000_007;
        int n = s.length();
        
        int prev = 0;
        int res = 0;

        for (int i = n - 1; i >= 0; i--) {
            int curr = 1;
            if (i < (n - 1) && s.charAt(i) == s.charAt(i+1)) {
                curr = (curr + prev) % m;
            }

            res = (res + curr) % m;
            prev = curr;
        }
        
        return res;
    }
}