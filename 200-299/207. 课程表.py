from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dd = defaultdict(list)
        indeg = [0] * numCourses
        res = 0
        for info in prerequisites:
            dd[info[1]].append(info[0])
            indeg[info[0]] += 1
        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        while q:
            res += 1
            u = q.popleft()
            for x in dd[u]:
                indeg[x] -= 1
                if indeg[x] == 0:
                    q.append(x)
        return res == numCourses
