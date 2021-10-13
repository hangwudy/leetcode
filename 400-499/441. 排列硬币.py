class Solution:
    def arrangeCoins(self, n: int) -> int:
        # if n < 4:
        #     return 1
        for i in range(0, n + 1):
            if (1 + i) * i / 2 > n:
                return i - 1
            elif (1 + i) * i / 2 == n:
                return i


so = Solution()
print(so.arrangeCoins(5))
print(so.arrangeCoins(8))
print(so.arrangeCoins(1))
print(so.arrangeCoins(2))
print(so.arrangeCoins(3))
print(so.arrangeCoins(4))
