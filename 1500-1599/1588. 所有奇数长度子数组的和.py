from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        preSum = [arr[0]]
        n = len(arr)
        for i in range(1, n):
            preSum.append(preSum[-1] + arr[i])
        ans = 0
        for i in range(n):
            for sz in range(1, n + 1 - i, 2):
                ans += preSum[i + sz] - preSum[i]
        return ans
