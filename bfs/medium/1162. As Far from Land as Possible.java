
class Solution {
    public int maxDistance(int[][] grid) {
        int ROWS = grid.length;
        int COLS = grid[0].length;

        ArrayDeque<int[]> queue = new ArrayDeque();
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 1) queue.offer(new int[] {r, c});
            }
        }

        if (queue.size() == 0 || queue.size() == ROWS * COLS) return -1;

        int[] dx = new int[] {0, 1, 0, -1};
        int[] dy = new int[] {1, 0, -1, 0};

        int dist = -1;

        while (!queue.isEmpty()) {
            int size = queue.size();
            dist++;

            for (int j = 0; j < size; j++) {
                int[] arr = queue.poll();
                int x = arr[0];
                int y = arr[1];

                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    if (0 <= nx && nx < ROWS && 0 <= ny && ny < COLS && grid[nx][ny] == 0) {
                        // mark as visited
                        grid[nx][ny] = 1;
                        queue.offer(new int[] {nx, ny});
                    }
                }
            }
        }

        return dist;
    }

}
