class Solution {
    public String pushDominoes(String dominoes) {
        Deque<Integer> dots = new ArrayDeque<>();
        int right = -1;

        int n = dominoes.length();
        char[] res = dominoes.toCharArray();

        for (int i = 0; i < n; i++) {
            char c = res[i];

            if (c == '.') {
                dots.addFirst(i);
            } else if (c == 'R') {
                if (!dots.isEmpty() && right != -1) {
                    while (!dots.isEmpty()) {
                        res[dots.removeLast()] = 'R';
                    }
                } else {
                    dots.clear();
                }
                right = i;

            } else {
                if (right == -1) {
                    while (!dots.isEmpty()) {
                        res[dots.removeFirst()] = 'L';
                    }
                } else {
                    int len = (i - right - 1) / 2;
                    for (int j = 0; j < len; j++) {
                        res[dots.removeFirst()] = 'L';
                        res[dots.removeLast()] = 'R';
                    }

                    dots.clear();
                    right = -1;
                }
            }
        }

        if (right != -1) {
            while (!dots.isEmpty()) {
                res[dots.removeLast()] = 'R';
            }
        }
        
        return new String(res);
    }
}