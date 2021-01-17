class Solution:
    def numWays(self, n: int) -> int:
        prev, curr, res = 0, 0, 1
        for i in range(n):
            prev, curr = curr, res
            res = prev + curr
        return res % 1000000007


so = Solution()
print(so.numWays(7))
