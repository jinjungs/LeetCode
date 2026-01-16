# Greedy
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        m = min(x, y)
        blocks = 2 * m + z
        if x != y:
            blocks += 1
        return blocks * 2

# DP: Bottom-up
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        # last: 0=AA, 1=BB, 2=AB, 3=START
        NEG = -10**9
        dp = [[[[NEG] * 4 for _ in range(z + 1)] for _ in range(y + 1)] for _ in range(x + 1)]
        dp[0][0][0][3] = 0

        ans = 0

        for a in range(x + 1):
            for b in range(y + 1):
                for c in range(z + 1):
                    for last in range(4):
                        cur = dp[a][b][c][last]
                        if cur == NEG:
                            continue
                        ans = max(ans, cur)

                        # Add AA: allowed after BB, AB, START (not after AA)
                        if a < x and last in (1, 2, 3):
                            dp[a + 1][b][c][0] = max(dp[a + 1][b][c][0], cur + 2)

                        # Add BB: allowed after AA, START (not after BB or AB)
                        if b < y and last in (0, 3):
                            dp[a][b + 1][c][1] = max(dp[a][b + 1][c][1], cur + 2)

                        # Add AB: allowed after BB, AB, START (not after AA)
                        if c < z and last in (1, 2, 3):
                            dp[a][b][c + 1][2] = max(dp[a][b][c + 1][2], cur + 2)

        return ans