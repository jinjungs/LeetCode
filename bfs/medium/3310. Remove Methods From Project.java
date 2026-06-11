class Solution {
    public List<Integer> remainingMethods(int n, int k, int[][] invocations) {
        // make graph
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] invoc: invocations) {
            int a = invoc[0];
            int b = invoc[1];
            graph.putIfAbsent(a, new ArrayList<>());
            graph.get(a).add(b);
        }

        // from k, mark suspicious node
        boolean[] suspicious = new boolean[n];
        Queue<Integer> q = new ArrayDeque<>();

        suspicious[k] = true;
        q.offer(k);

        while (!q.isEmpty()) {
            int node = q.poll();
            for (int nei : graph.getOrDefault(node, Collections.emptyList())) {
                if (!suspicious[nei]) {
                    suspicious[nei] = true;
                    q.offer(nei);
                }
            }
        }

        List<Integer> res = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (!suspicious[i] && graph.containsKey(i)) {
                for (int nei : graph.get(i)) {
                    if (suspicious[nei]) {
                        for (int j = 0; j < n; j++) {
                            res.add(j);
                        }   
                        return res;   
                    }
                }
            }
        }
        
        for (int i = 0; i < n; i++) {
            if (!suspicious[i]) res.add(i);
        }        

        return res;
    }
}