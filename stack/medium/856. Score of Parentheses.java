class Solution {
    public int scoreOfParentheses(String s) {
        Stack<Integer> stack = new Stack<>();
        int curr = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(curr);
                curr = 0;
            } else {
                if (curr == 0) {
                    curr++;
                } else {
                    curr *= 2;
                }
                curr += stack.pop();
            }

        }

        return curr;
    }
}