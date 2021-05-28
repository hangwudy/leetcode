class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        f = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            f[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i][j - 1]
                else:
                    minn = float('-inf')
                    for k in range(i, j):
                        minn = min(minn, f[i][k] + f[k + 1][j])
                    f[i][j] = minn
        return f[0][n - 1]
