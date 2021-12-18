from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = list(map(max, grid))
        col_max = list(map(max, zip(*grid)))
        return sum(min(row_max[i], col_max[j]) - h for i, row in enumerate(grid) for j, h in enumerate(row))
