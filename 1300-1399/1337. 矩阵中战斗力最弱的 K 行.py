from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = []
        for i, l, in enumerate(mat):
            m.append((sum(l), i))
        m.sort(key=lambda x: x[0])
        return [x[1] for x in m[:k]]


0
