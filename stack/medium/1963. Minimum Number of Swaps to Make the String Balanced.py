class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []

        for c in s:
            if stack and stack[-1] == '[' and c == ']':
                stack.pop()
            else:
                stack.append(c)

        pair = len(stack) // 2
        return pair // 2 + pair % 2