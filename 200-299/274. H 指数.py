from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        res = 1
        for c in citations:
            if c >= res:
                res += 1
        return res - 1


so = Solution()
print(so.hIndex([3, 0, 6, 1, 5]))
