from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_val = max(nums)

        total = [0] * (max_val + 1)
        for val in nums:
            total[val] += val

        def rob(nums):
            first = nums[0]
            second = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                first, second = second, max(second, first + nums[i])

            return second

        return rob(total)
