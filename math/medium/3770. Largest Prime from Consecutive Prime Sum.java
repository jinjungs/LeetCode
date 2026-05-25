class Solution {
    public int largestPrime(int n) {
        boolean[] isPrime = new boolean[n+1];
        Arrays.fill(isPrime, true);

        isPrime[0] = false;
        isPrime[1] = false;

        // sieve
        for (int i = 2; i * i <= n; i++) {
            if (!isPrime[i]) continue;
            
            for (int j = i * i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }

        int res = 0;
        int sum = 0;

        for (int i = 2; i <= n; i++) {
            if (!isPrime[i]) continue;
            sum += i;
            if (sum > n) break;
            if (isPrime[sum]) res = sum;
        }

        return res;
    }

}