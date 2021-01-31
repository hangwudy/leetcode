from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if self.is_similar(strs[i], strs[j]):
                    uf.union(i, j)
        return uf.set_cnt

    def is_similar(self, s1: str, s2: str) -> bool:
        cnt = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
        return cnt == 2 or cnt == 0


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.set_cnt = n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_y] > self.rank[root_x]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.rank[root_x] += self.rank[root_y]
        self.set_cnt -= 1
        return True

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
