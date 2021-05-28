from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in nums:
                current = num
                current_c = 1

                while current + 1 in nums:
                    current += 1
                    current_c += 1
                res = max(res, current_c)
        return res


so = Solution()
print(so.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(so.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
