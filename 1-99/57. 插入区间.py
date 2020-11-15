from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        placed = False
        ans = list()
        left, right = newInterval
        for le, ri in intervals:
            if le > right:
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([le, ri])
            elif ri < left:
                ans.append([le, ri])
            else:
                left = min(left, le)
                right = max(right, ri)
        if not placed:
            ans.append([left, right])
        return ans
