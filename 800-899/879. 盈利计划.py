from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        l = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(l + 1)]
        dp[0][0][0] = 1
        for i in range(1, l + 1):
            mem, earn = group[i - 1], profit[i - 1],
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    if j < mem:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - mem][max(0, k - earn)]) % MOD

        total = sum(dp[l][j][minProfit] for j in range(n + 1))
        return total % MOD
