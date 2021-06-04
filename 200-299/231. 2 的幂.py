class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        cnt = 0
        while n:
            n &= (n - 1)
            cnt += 1
        return cnt == 1


so = Solution()
print(so.isPowerOfTwo(5))
