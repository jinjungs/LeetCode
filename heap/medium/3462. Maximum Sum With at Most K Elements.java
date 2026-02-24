import java.util.*;

class Solution {
    public int minimumDeletions(String word, int k) {
        int n = word.length();

        Map<Character, Integer> map = new HashMap<>();
        for (int i=0; i < n; i++) {
            char key = word.charAt(i);
            map.put(key, map.getOrDefault(key, 0) + 1);
        }

        // {a: 4, c: 1, b: 2}
        // {a: 1, b: 2, c: 3, d: 5}
        // {a: 6, b: 1}

        int res = n;
        for (int freq = 0; freq < n+1; freq++) {
            // to meet (freq ~ freq + k), count remove
            int count = 0;
            for (Integer value: map.values()) {
                if (value < freq) {
                    count += value;
                } else if (value > freq + k) {
                    count += (value - freq - k);
                }
            }
            res = Math.min(res, count);
        }

        return res;

    }
}


class Solution {
    public int minimumDeletions(String word, int k) {
        int[] cnt = new int[26];
        for (int i = 0; i < word.length(); i++) {
            cnt[word.charAt(i) - 'a']++;
        }

        int[] freq = new int[26];
        int m = 0;
        for (int v : cnt) {
            if (v > 0) freq[m++] = v;
        }
        if (m == 0) return 0;

        Arrays.sort(freq, 0, m);

        int res = word.length();

        // base는 등장한 빈도 후보만 체크
        for (int i = 0; i < m; i++) {
            int base = freq[i];
            int upper = base + k;
            int del = 0;

            for (int j = 0; j < m; j++) {
                int v = freq[j];
                if (v < base) del += v;
                else if (v > upper) del += (v - upper);
            }
            res = Math.min(res, del);
        }

        return res;
    }
}