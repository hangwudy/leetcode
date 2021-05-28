from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(30):
            c = sum((val >> i) & 1 for val in nums)
            res += c * (n - c)
        return res


so = Solution()
print(so.totalHammingDistance([4, 14, 2]))
