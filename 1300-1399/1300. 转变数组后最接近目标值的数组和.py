from typing import List
from bisect import bisect_left


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        prefix = [0]
        for i in arr:
            prefix.append(prefix[-1] + i)

        r, ans, diff = arr[-1], 0, target
        for i in range(1, r + 1):
            it = bisect_left(arr, i)
            cur = prefix[it] + (n - it) * i
            if abs(cur - target) < diff:
                ans, diff = i, abs(cur - target)
        return ans


so = Solution()
print(so.findBestValue(arr=[4, 9, 3], target=10))
