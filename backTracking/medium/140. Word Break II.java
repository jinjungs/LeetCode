class Solution {
    List<String> res;
    Set<String> dict;
    String s;

    public List<String> wordBreak(String s, List<String> wordDict) {
        this.res = new ArrayList<>();
        this.s = s;
        this.dict = new HashSet<>();

        for (String word : wordDict) {
            dict.add(word);
        }

        backTrack(0, new ArrayList<>());
        return res;
    }

    private void backTrack(int idx, List<String> path) {
        if (idx == s.length()) {
            res.add(String.join(" ", path));
            return;
        }

        for (int i = idx; i < s.length(); i++) {
            String word = s.substring(idx, i+1);
            if (dict.contains(word)) {
                path.add(word);
                backTrack(i + 1, path);
                path.remove(path.size() - 1);
            }
        }
    }
}