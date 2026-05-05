class Solution {
    static final int MOD = 1_000_000_007;

    public int assignEdgeWeights(int[][] edges) {
        Arrays.sort(edges, (a, b) -> {
            if (a[0] == b[0]) {
                return a[1] - b[1];
            }
            return a[0] - b[0];
        });

        // graph
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < edges.length; i++) {
            int a = edges[i][0];
            int b = edges[i][1];
            graph.putIfAbsent(a, new ArrayList<>());
            graph.putIfAbsent(b, new ArrayList<>());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        // BFS -> depth
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> q = new ArrayDeque<>();
        
        q.offer(1);
        visited.add(1);

        int depth = -1;
        while (!q.isEmpty()) {
            int size = q.size();
            depth++;

            for (int i = 0; i < size; i++) {
                int node = q.poll();
                for (int nei: graph.getOrDefault(node, new ArrayList<>())) {
                    if (!visited.contains(nei)) {
                        visited.add(nei);
                        q.offer(nei);
                    }
                }
            }
        }

        // in order to be odd sum, there should be odd number of 1
        // -> half of cases
        // total cases: 2^depth
        // half of cases: 2^depth / 2 = 2^(depth-1)
        return modPow(2, depth - 1);
    }

    private int modPow(long base, int exp) {
        long res = 1;
        for (int i = 0; i < exp; i++) {
            res = (res * base) % MOD;
        }
        return (int) res;
    }
}