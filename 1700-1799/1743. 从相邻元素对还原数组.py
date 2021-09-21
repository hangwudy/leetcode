from typing import List
from collections import deque


class Solution1:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # dq = deque()
        n = len(adjacentPairs)
        init = adjacentPairs[0]
        dq = deque(init)
        adjacentPairs.pop(0)
        while adjacentPairs:
            for i in range(len(adjacentPairs)):
                l, r = adjacentPairs[i]
                if l in dq:
                    adjacentPairs.pop(i)
                    if dq[0] == l:
                        dq.appendleft(r)
                    else:
                        dq.append(r)
                    break
                elif r in dq:
                    adjacentPairs.pop(i)
                    if dq[0] == r:
                        dq.appendleft(l)
                    else:
                        dq.append(l)
                    break
                else:
                    continue
        return list(dq)


from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dd = defaultdict(list)
        for pair in adjacentPairs:
            l, r = pair
            dd[l].append(r)
            dd[r].append(l)
        n = len(adjacentPairs) + 1
        res = [0] * n
        for k, v in dd.items():
            if len(v) == 1:
                res[0] = k
                res[1] = v[0]
        for i in range(2, n):
            pair = dd[res[i - 1]]
            l, r = pair
            if res[i - 2] == l:
                res[i] = r
            else:
                res[i] = l
        return res


so = Solution()
print(so.restoreArray([[2, 1], [3, 4], [3, 2]]))
print(so.restoreArray([[4, -2], [1, 4], [-3, 1]]))
print(so.restoreArray([[100000, -100000]]))
#
# a = [[2, 1], [3, 4], [3, 2]]
# a.pop(2)
# print(a)
