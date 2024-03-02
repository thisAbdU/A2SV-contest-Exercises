class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                substr = ""
                while stack and stack[-1] != '[':
                    substr = stack.pop() + substr

                stack.pop()

                x = ""
                while stack and stack[-1].isdigit():
                    x = stack.pop() + x

                stack.append(int(x) * substr)
        
        return "".join(stack)