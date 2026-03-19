class Solution {
    public int robotSim(int[] commands, int[][] obstacles) {
        Set<String> obs = new HashSet<>();

        // store obstacles
        for (int[] o : obstacles) {
            obs.add(o[0] + "," + o[1]);
        }

        int[][] DIR = {{0,1}, {1,0}, {0,-1}, {-1,0}};
        int dir = 0;
        int x = 0, y = 0;
        int max = 0;

        for (int c : commands) {
            if (c == -1) {
                dir = (dir + 1) % 4;
            } else if (c == -2) {
                dir = (dir + 3) % 4;
            } else {
                for (int i = 0; i < c; i++) {
                    int nx = x + DIR[dir][0];
                    int ny = y + DIR[dir][1];

                    if (obs.contains(nx + "," + ny)) break;

                    x = nx;
                    y = ny;
                    max = Math.max(max, x*x + y*y);
                }
            }
        }

        return max;
    }
}