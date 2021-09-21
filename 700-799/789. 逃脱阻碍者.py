from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def m_distance(xy1, xy2):
            x1, y1 = xy1
            x2, y2 = xy2
            return abs(x1 - x2) + abs(y1 - y2)

        dis = m_distance([0, 0], target)
        return all([m_distance(ghost, target) > dis for ghost in ghosts])
