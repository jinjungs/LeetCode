class Solution {
    String res = "";
    int a;
    int b;

    public String findLexSmallestString(String s, int a, int b) {
        // apply a
        // if a == 1, the result will be changed 9 times
        // after rotated, the indices changed. so add 9 times more
        // rotate -> O(n)
        // compare two strings -> O(n)
        // O(n^2*18) -> brute force

        this.res = s;
        this.a = a;
        this.b = b;

        Set<String> visited = new HashSet<>();
        dfs(s, visited);

        return res;
    }

    private void dfs(String s, Set<String> visited) {
        if (visited.contains(s)) return;
        visited.add(s);

        if (s.compareTo(res) < 0){
            res = s;
        }

        dfs(rotate(s), visited);
        dfs(addA(s), visited);
    }

    private String rotate(String s) {
        if (s == null || "".equals(s) || s.length() == 1){
            return s;
        }
        
        int n = s.length();

        return s.substring(n-b, n) + s.substring(0, n-b);
    }

    private String addA(String s) {
        if (s == null || "".equals(s) || s.length() == 1){
            return s;
        }

        int n = s.length();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (i % 2 == 0) {
                sb.append(c);
            } else {
                int num = c - '0';
                num = (num + a) % 10;
                sb.append((char) (num + '0'));
            }
        }

        return sb.toString();
    }

}