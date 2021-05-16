from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def robRange(nums, start, end):
            first = nums[start]
            second = max(nums[start], nums[start + 1])
            for i in range(start + 2, end + 1):
                first, second = second, max(nums[i] + first, second),
            return second

        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        else:
            return max(robRange(nums, 0, n - 2), robRange(nums, 1, n - 1))
