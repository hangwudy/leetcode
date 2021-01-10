class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        i = 0
        n = len(s)
        sub_str = dict()
        for j in range(n):
            if s[j] in sub_str:
                i = max(i, sub_str[s[j]])
            ans = max(ans, j - i + 1)
            sub_str[s[j]] = j + 1
        return ans


so = Solution()
print(so.lengthOfLongestSubstring("abcabcbb"))
