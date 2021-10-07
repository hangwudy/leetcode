from typing import List
import heapq
import bisect


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        tmp = [float('-inf')] * 3
        heapq.heapify(tmp)
        if len(nums) < 3:
            return max(nums)
        for num in nums:
            if num > tmp[0]:
                heapq.heappop(tmp)
                heapq.heappush(tmp, num)
        return tmp[0]


class Solution1:
    def thirdMax(self, nums: List[int]) -> int:
        tmp = []
        for num in nums:
            if num not in tmp:
                bisect.insort(tmp, num)
                if len(tmp) > 3:
                    tmp.pop(0)
        return tmp[0] if len(tmp) == 3 else tmp[-1]


so = Solution1()
print(so.thirdMax([3, 2, 1]))
