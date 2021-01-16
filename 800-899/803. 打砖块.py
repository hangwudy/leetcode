from typing import List
from copy import deepcopy


class Solution:
    def __init__(self):
        self.DIRECTIONS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        self.rows = 0
        self.cols = 0

    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        self.rows = len(grid)
        self.cols = len(grid[0])

        # copy the original matrix
        dup = deepcopy(grid)
        # remove the hits in copy
        for hit in hits:
            dup[hit[0]][hit[1]] = 0

        size = self.rows * self.cols

        uf = UnionFind(size + 1)
        for j in range(self.cols):
            if dup[0][j] == 1:
                uf.union(j, size)

        for i in range(1, self.rows):
            for j in range(self.cols):
                if dup[i][j] == 1:
                    # check up
                    if dup[i - 1][j] == 1:
                        uf.union(self.get_index(i - 1, j), self.get_index(i, j))
                    # check left
                    if j > 0 and dup[i][j - 1] == 1:
                        uf.union(self.get_index(i, j - 1), self.get_index(i, j))
        hits_len = len(hits)
        res = [0] * hits_len
        for i in range(hits_len - 1, -1, -1):
            x = hits[i][0]
            y = hits[i][1]
            if grid[x][y] == 0:
                continue

            origin = uf.get_size(size)
            if x == 0:
                uf.union(y, size)

            for direction in self.DIRECTIONS:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if self.in_area(new_x, new_y) and dup[new_x][new_y] == 1:
                    uf.union(self.get_index(x, y), self.get_index(new_x, new_y))

            curr = uf.get_size(size)
            res[i] = max(0, curr - origin - 1)
            dup[x][y] = 1
        return res

    def get_index(self, x, y):
        return x * self.cols + y

    def in_area(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1 for _ in range(n)]

    def find(self, x: int):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        self.parent[root_x] = root_y
        self.size[root_y] += self.size[root_x]

    def get_size(self, x):
        root = self.find(x)
        return self.size[root]


so = Solution()
print(so.hitBricks([[1, 0, 0, 0], [1, 1, 1, 0]],
                   [[1, 0]]))
