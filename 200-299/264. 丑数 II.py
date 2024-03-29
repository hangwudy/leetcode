class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * (n + 1)
        p2, p3, p5 = 1, 1, 1
        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            elif dp[i] == num3:
                p3 += 1
            else:
                p5 += 1
        return dp[n]


so = Solution()
print(so.nthUglyNumber(3))
