from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        s = sum(stones)
        t = s // 2
        f = [[0] * (t + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            x = stones[i - 1]
            for j in range(t + 1):
                f[i][j] = f[i - 1][j]
                if j >= x:
                    f[i][j] = max(f[i][j], f[i - 1][j - x] + x)
        return abs(s - f[n][t] - f[n][t])
