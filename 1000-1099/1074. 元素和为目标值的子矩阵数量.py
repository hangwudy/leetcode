from typing import List
from collections import defaultdict


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for i in range(m):
            total = [0] * n
            for j in range(i, m):
                for c in range(n):
                    total[c] += matrix[j][c]
                ans += self.calc(total, target)
        return ans

    def calc(self, nums, k):
        mp = defaultdict(int)
        mp[0] = 1
        pre = 0
        count = 0
        for i in range(len(nums)):
            pre += nums[i]
            if pre - k in mp:
                count += mp[pre - k]
            mp[pre] += 1
        return count


so = Solution()
print(so.numSubmatrixSumTarget(matrix=[[1, -1], [-1, 1]], target=0))
