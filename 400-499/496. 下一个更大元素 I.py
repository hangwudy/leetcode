from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hmap = dict()
        for num in nums2:
            while stack and stack[-1] < num:
                hmap[stack.pop()] = num
            stack.append(num)
        res = []
        for n in nums1:
            res.append(hmap.get(n, -1))
        return res


so = Solution()
print(so.nextGreaterElement([1, 3, 5, 2, 4],
                            [6, 5, 4, 3, 2, 1, 7]))
