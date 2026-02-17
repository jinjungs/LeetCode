class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cost = [abs(ord(s[x]) - ord(t[x])) for x in range(n)]

        maxLen = 0
        currCost = 0
        l = 0

        for r in range(n):
            currCost += cost[r]

            while currCost > maxCost:
                currCost -= cost[l]
                l += 1

            maxLen = max(maxLen, r - l + 1)

        return maxLen