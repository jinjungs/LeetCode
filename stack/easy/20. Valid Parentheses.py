class Solution:
    def isValid(self, s: str) -> bool:
        p_list = []

        def match(ch) -> str:
            if ch == ')':
                return '('
            elif ch == '}':
                return '{'
            elif ch == ']':
                return '['

        def start(ch) -> bool:
            return ch in ['(','{','[']

        def end(ch) -> bool:
            return ch in [')','}',']']

        if end(s[0]):
            return False
        if start(s[-1]):
            return False

        for i in range(len(s)):
            ch = s[i]
            if len(p_list) == 0 or start(ch):
                p_list.append(ch)
                continue

            last = p_list[-1]
            if match(ch) != last:
                return False
            else:
                p_list.pop()

        return len(p_list) == 0