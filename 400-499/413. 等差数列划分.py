from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        t = 0
        ans = 0
        d = nums[1] - nums[0]
        for i in range(2, n):
            if nums[i] - nums[i - 1] == d:
                t += 1
            else:
                d = nums[i] - nums[i - 1]
                t = 0
            ans += t
        return ans


so = Solution()
print(so.numberOfArithmeticSlices([1, 2, 3, 4]))
