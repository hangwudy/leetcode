from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        start = 0
        end = 0
        target = 0
        ans = n + 1
        while end < n:
            target += nums[end]
            while target >= s:
                ans = min(ans, end - start + 1)
                target -= nums[start]
                start += 1
            end += 1

        return 0 if ans == n + 1 else ans


so = Solution()
print(so.minSubArrayLen(s=7, nums=[2, 3, 1, 2, 4, 3]))
