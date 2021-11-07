class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        r_min = c_min = 40001
        for l in ops:
            r, c = l
            r_min = min(r_min, r)
            c_min = min(c_min, c)
        return r_min * c_min