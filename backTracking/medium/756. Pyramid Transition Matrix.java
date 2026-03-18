class Solution {
    public boolean pyramidTransition(String bottom, List<String> allowed) {
        Map<String, List<Character>> map = new HashMap<>();
        for (String s : allowed) {
            String key = s.substring(0, 2);
            map.putIfAbsent(key, new ArrayList<>());
            map.get(key).add(s.charAt(2));
        }

        return dfs(bottom, map);
    }

    private boolean dfs(String bottom, Map<String, List<Character>> map) {
        if (bottom.length() == 1) return true;

        List<String> nextLevels = new ArrayList<>();
        buildNextLevels(bottom, 0, new StringBuilder(), nextLevels, map);

        for (String next : nextLevels) {
            if (dfs(next, map)) return true;
        }

        return false;
    }

    private void buildNextLevels(
        String bottom,
        int idx,
        StringBuilder path,
        List<String> nextLevels,
        Map<String, List<Character>> map
    ) {
        // Finished building one next row
        if (idx == bottom.length() - 1) {
            nextLevels.add(path.toString());
            return;
        }

        String key = bottom.substring(idx, idx + 2);
        if (!map.containsKey(key)) return;

        for (char c : map.get(key)) {
            path.append(c);
            buildNextLevels(bottom, idx + 1, path, nextLevels, map);
            path.deleteCharAt(path.length() - 1);
        }
    }
}