from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        uf = UnionFind(n)

        for x, y in connections:
            uf.union(x, y)

        return uf.set_num - 1


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.set_num = n
        self.rank = [1] * n

    def find(self, x: int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] > self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_x] = root_y
        self.rank[root_y] += self.rank[root_x]
        self.set_num -= 1
        return True

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
