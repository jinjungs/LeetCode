class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        res = 0
        cnt = 0

        for ch in s:
            if ch == '1':
                cnt += 1
                res += cnt          # 핵심: 끝이 현재 위치인 1-부분문자열 개수
            else:
                cnt = 0

        return res % MOD