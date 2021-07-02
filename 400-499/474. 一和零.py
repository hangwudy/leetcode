from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for __ in range(l + 1)]
        for i in range(1, l + 1):
            zeros, ones = self.get_zeros_ones(strs[i - 1])
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if j >= zeros and k >= ones:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - zeros][k - ones] + 1)
        return dp[-1][-1][-1]

    def get_zeros_ones(self, s):
        z_o = [0, 0]
        for i in s:
            z_o[ord(i) - ord("0")] += 1
        return z_o
