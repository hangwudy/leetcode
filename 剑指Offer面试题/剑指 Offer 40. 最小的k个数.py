from typing import List
import heapq


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in arr[k:]:
            if -hp[0] > i:
                heapq.heappop(hp)
                heapq.heappush(hp, -i)

        return [-i for i in hp]


so = Solution()
print(so.getLeastNumbers(arr=[3, 2, 1], k=2))
