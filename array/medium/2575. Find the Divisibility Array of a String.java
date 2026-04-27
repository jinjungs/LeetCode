class Solution {
    public int[] divisibilityArray(String word, int m) {
        int n = word.length();
        int[] div = new int[n];
        long curr = 0;

        for (int i = 0; i < n; i++) {
            long num = (long) (word.charAt(i) - '0');
            curr = (curr * 10 + num) % m;
            div[i] = (curr == 0) ? 1 : 0;
        }

        return div;
    }
}