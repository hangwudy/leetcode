from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        def get_num(i):
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]

        ans = -1
        while right >= left:
            mid = left + (right - left) // 2
            if get_num(mid - 1) < get_num(mid) > get_num(mid + 1):
                return mid
            elif get_num(mid) < get_num(mid + 1):
                left = mid + 1
            else:
                right = mid - 1
        return ans
   