class Solution {
    public boolean areSentencesSimilar(String sentence1, String sentence2) {
        String[] s1 = sentence1.split(" ");
        String[] s2 = sentence2.split(" ");

        return isSimilar(s1, s2);
    }

    private boolean isSimilar(String[] s1, String[] s2) {
        if (s1.length > s2.length) {
            return isSimilar(s2, s1);
        }

        int l = 0;
        while (l < s1.length && s1[l].equals(s2[l])) {
            l++;
        }

        int r = 0;
        while (r < s1.length - l && 
            s1[s1.length - 1 - r].equals(s2[s2.length - 1 - r])) {
            r++;
        }

        return l + r == s1.length;
    }
}