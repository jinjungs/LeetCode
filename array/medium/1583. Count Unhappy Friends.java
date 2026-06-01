class Solution {
    int[] pairArr;
    int[][] preferences;

    public int unhappyFriends(int n, int[][] preferences, int[][] pairs) {
        this.preferences = preferences;
        this.pairArr = new int[n];

        for (int[] pair : pairs) {
            int x = pair[0];
            int y = pair[1];
            pairArr[x] = y;
            pairArr[y] = x;
        }

        int res = 0;

        for (int x = 0; x < n; x++) {            
            if (isUnhappy(x)) res++;
        }
        
        return res;
    }

    private boolean isUnhappy(int x) {
        int y = pairArr[x];
        
        for (int u : preferences[x]) {
            if (u == y) break;

            int v = pairArr[u];
            
            // if u prefers x over v, x is unhappy
            for (int candidate: preferences[u]) {
                if (candidate == x) return true;
                if (candidate == v) break;
            }
        }

        return false;
    }
}