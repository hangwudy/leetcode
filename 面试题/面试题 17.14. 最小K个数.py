"""
输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]
"""

from typing import List
import heapq


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()
        hq = [float("-inf")] * k
        heapq.heapify(hq)
        for a in arr:
            if -hq[0] > a:
                heapq.heappop(hq)
                heapq.heappush(hq, -a)
        return [-x for x in hq]


so = Solution()
print(so.smallestK(arr=[1, 3, 5, 7, 2, 4, 6, 8], k=4))
