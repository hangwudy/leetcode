from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not nums:
            return []
        tmp = []
        for i in nums:
            tmp += i
        if len(tmp) != r * c:
            return nums
        res = []
        for n in range(r):
            res.append(tmp[n * c:n * c + c])
        return res
        # print(res)


so = Solution()
print(so.matrixReshape(nums=
                       [[1, 2],
                        [3, 4]], r=1, c=4))
