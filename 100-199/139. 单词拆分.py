from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True

        return dp[-1]


so = Solution()
print(so.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
