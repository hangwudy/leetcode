from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        edges = list()
        for i in range(m):
            for j in range(n):
                index = i * n + j
                if i > 0:
                    edges.append((index - n, index, max(grid[i][j], grid[i - 1][j])))
                if j > 0:
                    edges.append((index - 1, index, max(grid[i][j], grid[i][j - 1])))
        edges.sort(key=lambda x: x[2])
        res = 0
        uf = UnionFind(m * n)
        for start, end, height in edges:
            uf.union(start, end)
            res = max(res, height)
            if uf.is_connected(0, m * n - 1):
                break
        return res


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
        root_x, root_y = self.find(x), self.find(y),
        if root_x == root_y:
            return False
        if self.rank[root_y] < self.rank[root_x]:
            root_x, root_y = root_y, root_x
        self.parent[root_x] = root_y
        self.rank[root_y] += self.rank[root_x]
        self.set_cnt -= 1
        return True

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
