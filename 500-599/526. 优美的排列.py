from collections import defaultdict


class Solution:
    def countArrangement(self, n: int) -> int:
        match = defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i % j == 0 or j % i == 0:
                    match[i].append(j)
        num = 0
        vis = set()

        def backtrack(index):
            if index == n + 1:
                nonlocal num
                num += 1
                return

            for x in match[index]:
                if x not in vis:
                    vis.add(x)
                    backtrack(index + 1)
                    vis.discard(x)

        backtrack(1)
        return num
