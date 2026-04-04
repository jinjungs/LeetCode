class Solution {
    public String maxValue(String n, int x) {
        int sign = 1;
        StringBuilder sb = new StringBuilder();
        int idx = -1;

        for (int i = 0; i < n.length(); i++) {
            char c = n.charAt(i);

            if (i == 0 && c == '-') {
                sign = -1;
                sb.append(c);
                continue;
            }
            
            int num = c - '0';
            
            if ((sign > 0 && num < x) || (sign < 0 && num > x)) {
                sb.append(x);
                idx = i;
                break;
            }

            sb.append(c);
        }

        if (idx == -1) {
            sb.append(x);
        } else {
            for (int i = idx; i < n.length(); i++) {
                sb.append(n.charAt(i));
            }
        }

        return sb.toString();
    }
}