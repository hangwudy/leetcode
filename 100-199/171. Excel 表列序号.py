class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        base = ord("A")
        n = len(columnTitle)
        p = 0
        res = 0
        while n:
            res += (ord(columnTitle[n - 1]) - base + 1) * 26 ** p
            p += 1
            n -= 1
        return res


so = Solution()
print(so.titleToNumber("AA"))
print(so.titleToNumber("AB"))
print(so.titleToNumber("B"))
print(so.titleToNumber("ZY"))
print(so.titleToNumber("FXSHRXW"))
