class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] == 1 || grid[n-1][n-1] == 1) return -1;

        // bfs
        int[] dx = new int[] {1,1,0,-1,-1,-1,0,1};
        int[] dy = new int[] {0,-1,-1,-1,0,1,1,1};

        Queue<int[]> q = new ArrayDeque<>();
        grid[0][0] = -1;
        q.offer(new int[]{0,0});

        int len = 1;
        while (!q.isEmpty()) {
            int size = q.size();
            for (int j = 0; j < size; j++) {
                int[] pos = q.poll();
                int x = pos[0], y = pos[1];

                if (x == n-1 && y == n-1) return len;

                for (int i = 0; i < 8; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if (nx >= 0 && nx < n && ny >= 0 && ny < n && grid[nx][ny] == 0) {
                        grid[nx][ny] = -1;
                        q.offer(new int[] {nx, ny});
                    }
                }
            }
            len++;
        }

        return -1;

    }
}