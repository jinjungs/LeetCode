from typing import List


class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        dp = [0] * n
        stack = []
        maxBooks = 0

        for i in range(n):
            while stack and books[stack[-1]] >= books[i] - (i - stack[-1]):
                stack.pop()

            if not stack:
                length = i + 1
                first = max(0, books[i] - i)
                dp[i] = (books[i] + first) * (books[i] - first + 1) // 2
            else:
                j = stack[-1]
                length = i - j
                first = max(0, books[i] - (i - j - 1))
                dp[i] = dp[j] + (books[i] + first) * (books[i] - first + 1) // 2

            maxBooks = max(maxBooks, dp[i])
            stack.append(i)

        return maxBooks