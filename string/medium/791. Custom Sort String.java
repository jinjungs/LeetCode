class Solution {
    public String customSortString(String order, String s) {
        // plan
        // make count arr: count s char
        // iterate order
        // order[i] in count, res += c * count[c]

        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
        }

        // append character in order
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < order.length(); i++) {
            char c = order.charAt(i);
            int idx = c - 'a';
            for (int j = 0; j < count[idx]; j++) {
                sb.append(c);
            }
            count[idx] = 0;
        }

        // append character not in order
        for (int i = 0; i < count.length; i++) {
            for (int j = 0; j < count[i]; j++) {
                sb.append((char)(i + 'a'));
            }
        }

        return sb.toString();
    }
}