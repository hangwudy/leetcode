from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hmap = dict()
        hmap[0] = -1
        pre_sum = 0
        res = 0
        for i, num in enumerate(nums):
            if num == 1:
                pre_sum += num
            else:
                pre_sum -= num
            if pre_sum in hmap:
                res = max(res, i - hmap[num])
            else:
                hmap[num] = i
        return res
