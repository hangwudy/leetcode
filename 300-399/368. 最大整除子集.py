from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1] * n
        max_size = 1
        max_val = dp[0]
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)

            if dp[i] > max_size:
                max_size = dp[i]
                max_val = nums[i]
        res = []
        if max_size == 1:
            res.append(nums[0])
            return res

        i = n - 1
        while i >= 0 and max_size > 0:
            if dp[i] == max_size and max_val % nums[i] == 0:
                res.append(nums[i])
                max_val = nums[i]
                max_size -= 1
            i -= 1
        return res
