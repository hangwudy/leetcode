from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        res = []
        path = []
        used = [False] * size
        self.dfs(nums, size, 0, path, used, res)
        return res

    def dfs(self, nums, size, depth, path, used, res):
        if depth == size:
            res.append(path.copy())
            return
        for i, n in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(n)
            self.dfs(nums, size, depth + 1, path, used, res)
            used[i] = False
            path.pop()


so = Solution()
print(so.permute([1, 2, 3]))
