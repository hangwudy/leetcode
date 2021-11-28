from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        d = timeSeries[0] + duration
        for t in timeSeries[1:]:
            if t > d:
                res += duration
            else:
                res += t - d + duration
            d = t + duration
        res += duration
        return res


so = Solution()
# print(so.findPoisonedDuration(timeSeries=[1, 4], duration=2))
# print(so.findPoisonedDuration(timeSeries=[1, 4], duration=2))
print(so.findPoisonedDuration(timeSeries=[1, 2, 3, 4, 5], duration=5))
