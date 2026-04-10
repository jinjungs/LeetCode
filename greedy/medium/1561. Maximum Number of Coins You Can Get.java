class Solution {
    public int maxCoins(int[] piles) {
            int cnt = piles.length / 3;
            Arrays.sort(piles);

            int res = 0;
            for (int i = cnt; i < piles.length; i = i + 2) {
                res += piles[i];
            }

            return res;
    }
}