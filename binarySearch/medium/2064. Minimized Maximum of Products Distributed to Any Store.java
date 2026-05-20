class Solution {
    public int minimizedMaximum(int n, int[] quantities) {
        int m = quantities.length;
        
        int maxQuant = 0;
        for (int quant : quantities) {
            maxQuant = Math.max(maxQuant, quant);
        }

        if (m == n) return maxQuant;

        int res = Integer.MAX_VALUE;
        int l = 1;
        int r = maxQuant;

        while (l <= r) {
            int maxCntPerStore = l + (r - l) / 2;
            
            // count stores
            int stores = 0;
            for (int quant : quantities) {
                stores += (int) (Math.ceil((double) quant / maxCntPerStore));
            }

            if (stores > n) {
                l = maxCntPerStore + 1;
            } else {
                res = maxCntPerStore;
                r = maxCntPerStore - 1;
            }
        }

        return res;
    }
}