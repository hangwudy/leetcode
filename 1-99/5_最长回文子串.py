class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        # palindrome
        m = ""
        # left 2 right, O = n
        for i in range(len(s)):
            # right 2 left, O = n
            for j in range(len(s)-1, i-1, -1):
                if len(m) > j - i:
                    break
                elif s[i:j] == s[j:i:-1]:
                    m = s[i:j+1]
        return m


so = Solution()
print(so.longestPalindrome("babad"))
