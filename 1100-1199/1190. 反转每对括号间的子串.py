class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        res = ""
        for c in s:
            if c == "(":
                stack.append(res)
                res = ""
            elif c == ")":
                res = stack.pop() + res[::-1]
            else:
                res += c
        return res


so = Solution()
print(so.reverseParentheses("(a(bc)d)"))
