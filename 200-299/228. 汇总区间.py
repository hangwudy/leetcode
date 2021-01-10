from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        i = 0
        res = []
        while i < n:
            low = i
            i += 1
            while i < n and nums[i] == nums[i - 1] + 1:
                i += 1
            high = i - 1
            if low < high:
                tmp = str(nums[low]) + "->" + str(nums[high])
            else:
                tmp = str(nums[low])
            res.append(tmp)
        return res


so = Solution()
print(so.summaryRanges([0, 1, 2, 4, 5, 7]))
