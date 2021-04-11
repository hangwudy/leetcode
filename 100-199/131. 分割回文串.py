from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = s[i] == s[j] and f[i + 1][j - 1]
        ans = []
        ret = []

        def dfs(idx):
            if idx == n:
                ret.append(ans[:])
                return
            for i in range(idx, n):
                if f[idx][i]:
                    ans.append(s[idx:i + 1])
                    dfs(i + 1)
                    ans.pop()

        dfs(0)
        return ret


so = Solution()
print(so.partition("aab"))
print(so.partition("aa"))
