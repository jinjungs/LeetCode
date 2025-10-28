class Solution {
    public String decodeString(String s) {
        if (s == null || s.isEmpty() || s.length() <= 1) {
            return s;
        }
        
        int n = s.length();
        int numStart = 0;
        while (numStart < n && !Character.isDigit(s.charAt(numStart))) {
            numStart++;
        }

        // no number
        if (numStart == n) {
            return s;
        }

        // '['와 ']' 위치 찾기
        int braStart = -1;
        int braEnd = -1;
        int cnt = 0;

        for (int i = numStart; i < n; i++) {
            if (s.charAt(i) == '[') {
                if (cnt == 0) braStart = i; // 첫 '[' 기록
                cnt++;
            } else if (s.charAt(i) == ']') {
                cnt--;
                if (cnt == 0) { // 짝 맞으면 끝
                    braEnd = i;
                    break;
                }
            }
        }

        int num = Integer.parseInt(s.substring(numStart, braStart));
        String inner = decodeString(s.substring(braStart+1, braEnd));
        String decoded = inner.repeat(num);
        
        return s.substring(0, numStart) + decoded + decodeString(s.substring(braEnd+1));

    }
    
}