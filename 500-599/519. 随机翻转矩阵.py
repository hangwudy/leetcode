import random
from typing import List


class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.hashmap = {}

    def flip(self) -> List[int]:
        x = random.randint(0, self.total - 1)
        self.total -= 1
        idx = self.hashmap.get(x, x)
        self.hashmap[x] = self.hashmap.get(self.total, self.total)
        return [idx // self.n, idx % self.n]

    def reset(self) -> None:
        self.total = self.m * self.n
        self.hashmap.clear()

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
