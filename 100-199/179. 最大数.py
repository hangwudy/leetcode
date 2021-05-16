from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber2(self, nums: List[int]) -> str:
        def compare(x, y):
            return int(y + x) - int(x + y)

        nums = sorted(map(str, nums), key=cmp_to_key(compare))
        if nums[0] == "0":
            return "0"
        return "".join(nums)

    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        compare = lambda x, y: 1 if x + y < y + x else -1
        nums.sort(key=cmp_to_key(compare))
        if nums[0] == "0":
            return "0"
        return "".join(nums)


so = Solution()
print(so.largestNumber([10, 2]))
