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


// memoization
class Solution {
    Set<String> dict;
    String s;
    List<String>[] memo;

    public List<String> wordBreak(String s, List<String> wordDict) {
        this.s = s;
        this.dict = new HashSet<>();
        this.memo = new List[s.length() + 1];

        for (String word : wordDict) {
            dict.add(word);
        }

        return backTrack(0);
    }

    private List<String> backTrack(int idx) {
        if (memo[idx] != null) {
            return memo[idx];
        }

        List<String> sentences = new ArrayList<>();

        if (idx == s.length()) {
            sentences.add("");
            return memo[idx] = sentences;
        }

        for (int end = idx + 1; end <= s.length(); end++) {
            String word = s.substring(idx, end);

            if (!dict.contains(word)) continue;

            for (String suffix : backTrack(end)) {
                sentences.add(suffix.isEmpty() ? word : word + " " + suffix);
            }
        }

        return memo[idx] = sentences;
    }
}