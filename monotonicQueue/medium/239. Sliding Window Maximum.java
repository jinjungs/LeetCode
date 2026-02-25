// First Solution
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> stack = new ArrayDeque<>();
        int n = nums.length;
        int[] res = new int[n-k+1];

        for (int i = 0; i < n; i++) {
            // push max candidates
            while (!stack.isEmpty() && stack.peek() < nums[i]) {
                stack.pop();
            }
            stack.push(nums[i]);

            if (i < k-1) continue;

            // pop
            if (i-k >= 0 && stack.peekLast() <= nums[i-k]) {
                stack.pollLast();
            }

            res[i-k+1] = stack.peekLast();
        }

        return res;
    }
}

// Good Solution
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        int[] res = new int[n - k + 1];
        Deque<Integer> dq = new ArrayDeque<>(); // stores indices

        for (int i = 0; i < n; i++) {
            // 1) Remove indices out of window [i-k+1, i]
            while (!dq.isEmpty() && dq.peekFirst() <= i - k) {
                dq.pollFirst();
            }

            // 2) Maintain decreasing order by value
            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) {
                dq.pollLast();
            }

            // 3) Add current index
            dq.addLast(i);

            // 4) Record answer when window is formed
            if (i >= k - 1) {
                res[i - k + 1] = nums[dq.peekFirst()];
            }
        }

        return res;
    }
}