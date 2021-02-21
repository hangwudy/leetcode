from typing import List
import bisect


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        left = right = 0
        max_len = 0
        span = []
        while left < n and right < n:
            bisect.insort(span, nums[right])
            if abs(span[0] - span[-1]) > limit:
                # max_len = max(right - left, max_len)
                span.remove(nums[left])
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len


so = Solution()
print(so.longestSubarray(nums=[8, 2, 4, 7], limit=4))
print(so.longestSubarray(nums=[10, 1, 2, 4, 7, 2], limit=5))
print(so.longestSubarray(nums=[4, 2, 2, 2, 4, 4, 2, 2], limit=0))
