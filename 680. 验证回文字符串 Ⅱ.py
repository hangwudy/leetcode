class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while r > l:
            if s[l] != s[r]:
                return self.checkPalindrom(l + 1, r, s) or self.checkPalindrom(l, r - 1, s)
            else:
                l += 1
                r -= 1
        return True

    def checkPalindrom(self, left, right, s):
        while right > left:
            if s[left] != s[right]:
                return False
            right -= 1
            left += 1
        return True


so = Solution()
print(so.validPalindrome("atweta"))
