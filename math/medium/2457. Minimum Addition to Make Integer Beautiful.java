class Solution {
    public long makeIntegerBeautiful(long n, int target) {
        long original = n;
        long base = 10;

        while (digitSum(n) > target) {
            long add = base - (n % base);
            n += add;
            base *= 10;
        }

        return n - original;
    }

    public long digitSum(long num) {
        long sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}