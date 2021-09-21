from typing import List
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dd = defaultdict(list)
        indeg = [0] * numCourses
        for info in prerequisites:
            dd[info[1]].append(info[0])
            indeg[info[0]] += 1
        res = []
        q = deque([u for u in range(numCourses) if indeg[u] == 0])
        while q:
            u = q.popleft()
            res.append(u)
            for x in dd[u]:
                indeg[x] -= 1
                if indeg[x] == 0:
                    q.append(x)

        return res if len(res) == numCourses else []
