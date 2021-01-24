from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        stack = list()
        res = 0
        for num in nums:
            if stack:
                if num <= stack[-1]:
                    res = max(len(stack), res)
                    stack.clear()

            stack.append(num)
        res = max(len(stack), res)
        return res


so = Solution()
print(so.findLengthOfLCIS([1, 3, 5, 7]))
