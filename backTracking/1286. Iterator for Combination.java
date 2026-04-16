class CombinationIterator {
    char[] words;
    int n;
    List<String> comb = new ArrayList<>();
    int curr;

    public CombinationIterator(String characters, int combinationLength) {
        words = characters.toCharArray();
        Arrays.sort(words);

        this.n = combinationLength;
        this.curr = 0;
        backTrack(0, new StringBuilder());
    }
    
    public String next() {
        return comb.get(curr++);
    }
    
    public boolean hasNext() {
        return curr < comb.size();
    }

    private void backTrack(int idx, StringBuilder path) {
        if (path.length() == this.n) {
            comb.add(path.toString());
            return;
        }

        if (idx >= words.length) return;

        path.append(this.words[idx]);
        backTrack(idx+1, path);
        path.deleteCharAt(path.length() - 1);
        backTrack(idx+1, path);
    }
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator obj = new CombinationIterator(characters, combinationLength);
 * String param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */