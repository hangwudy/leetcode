import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        return right - left
