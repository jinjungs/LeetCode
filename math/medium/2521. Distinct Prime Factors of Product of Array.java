class Solution {
    public int distinctPrimeFactors(int[] nums) {
        Set<Integer> primes = new HashSet<>();

        for (int num : nums) {
            int curr = num;
            for (int factor = 2; factor * factor <= curr; factor++) {
                while (curr % factor == 0) {
                    primes.add(factor);
                    curr /= factor;
                }
            }

            if (curr > 1) {
                primes.add(curr);
            }
        }

        return primes.size();
    }
}