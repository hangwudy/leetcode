from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        def isSorted():
            for i in range(1, n):
                if nums[i] < nums[i - 1]:
                    return False
            return True

        if isSorted():
            return 0

        sorted_nums = sorted(nums)
        left = 0
        while nums[left] == sorted_nums[left]:
            left += 1
        right = n - 1
        while nums[right] == sorted_nums[right]:
            right -= 1
        return right - left + 1
