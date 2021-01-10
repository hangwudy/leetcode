from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n_len = len(nums)

        for i in range(1, n_len):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]

        return max(nums)


so = Solution()
print(so.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
