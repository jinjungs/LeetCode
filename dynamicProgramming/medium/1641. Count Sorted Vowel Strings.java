class Solution {
    public int countVowelStrings(int n) {
        // 5 + 4 + 3 + 2 + 1
        // n = 3
        // (a ~ u까지 2자리 조합) + (e ~ u까지 2자리 조합) + (i ~ u까지 ) ...
        // 1 1 1 1 1 
        // 5 4 3 2 1
        // 15 10 6 3 1

        int[] vowels = new int[] {1,1,1,1,1};
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < 5; j++) {
                if (j > 0) {
                    vowels[j] += vowels[j-1];
                }
            }            
        }

        int res = 0;
        for (int i = 0; i < 5; i++) {
            res += vowels[i];
        }      

        return res;
    }
}