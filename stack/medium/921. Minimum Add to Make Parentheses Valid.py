class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for c in s:
            if not stack or c == '(' or stack[-1] != '(':
                stack.append(c)
            else:
                stack.pop()

        return len(stack)