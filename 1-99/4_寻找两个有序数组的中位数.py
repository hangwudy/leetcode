from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()
        n = len(num)
        if n % 2 == 0:
            ans = (num[n//2] + num[n//2 - 1]) / 2
        else:
            ans = num[n//2]
        return ans

so = Solution()
print(so.findMedianSortedArrays([1, 3], [3, 4]))