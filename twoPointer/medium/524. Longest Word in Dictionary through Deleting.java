class Solution {
    public String findLongestWord(String s, List<String> dictionary) {
        String best = "";

        for (String w : dictionary) {
            if (!isSubseq(s, w)) continue;

            if (w.length() > best.length() ||
                (w.length() == best.length() && w.compareTo(best) < 0)) {
                best = w;
            }
        }

        return best;
    }

    private boolean isSubseq(String s, String w) {
        int i = 0;
        for (int j = 0; j < s.length() && i < w.length(); j++) {
            if (s.charAt(j) == w.charAt(i)) i++;
        }
        return i == w.length();
    }
}