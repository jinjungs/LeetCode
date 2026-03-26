    class Solution {
    public int bestTeamScore(int[] scores, int[] ages) {
        // sort by age, bigger score
        // (4,2) (5,1) (6,2) (5,1)
        // (5,1) (5,1) (4,2) (6,2)
        // score needs to be increased as the age goes up
        // (1,5) (1,5) (2,4) (2,6)
        // dp[i]: best sum of scores till ith

        // what if have multiple scroes in same age?
        // monotonic stack
        // (1,5) (1,5) (2,6) (2,10) (3,7) (3,20)
        // (1,5) 5
        // if prevAge == age, add
        // (1,5) (1,5) 10
        // prevAge < age and prevScore < score, add
        // (1,5) (1,5) (2,6) 16 
        // (1,5) (1,5) (2,6) (2,10) 26
        // while prevAge < age and prevScore >= score, pop
        // add
        // (1,5) (1,5) (2,6) (3,7) 23

        // (1,5) (1,5) (2,6) (3,7) (3,20) 43
        // (1,5) (1,5) (2,6) (2,10) (3,20) 46 <- (2,10) come back, how?
        // check previous dp[i]
        // if pairs[j][0] == pairs[i][0] && pairs[j][1] <= pairs[i][1]
        // or pairs[j][0] < pairs[i][0] && pairs[j][1] < pairs[i][1]
        // dp[i] = Math.max(dp[i], dp[j] + pairs[i][1])

        // make pairs
        int n = scores.length;
        int[][] pairs = new int[n][2];

        for (int i = 0; i < n; i++) {
            pairs[i] = new int[] {ages[i], scores[i]};
        }

        // sort
        Arrays.sort(pairs, (a, b) -> {
            if (a[0] == b[0]) {
                return Integer.compare(a[1], b[1]); // second key
            }
            return Integer.compare(a[0], b[0]); // first key
        });

        int[] dp = new int[n];
        int bestScore = 0;

        for (int i = 0; i < n; i++) {
            int age = pairs[i][0];
            int score = pairs[i][1];
            dp[i] = score;

            // compare previous value
            for (int j = i-1; j >= 0; j--) {
                int prevAge = pairs[j][0];
                int prevScore = pairs[j][1];

                if (prevScore <= score) {
                    dp[i] = Math.max(dp[i], dp[j] + score);
                }
            }
            
            bestScore = Math.max(bestScore, dp[i]);
        }

        return bestScore;

    }
}