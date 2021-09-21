from typing import List
import bisect
import random


class Solution:

    def __init__(self, w: List[int]):
        self.preSum = [w[0]]
        n = len(w)
        for i in range(1, n):
            self.preSum.append(self.preSum[-1] + w[i])

    def pickIndex(self) -> int:
        x = random.randint(1, self.preSum[-1])
        return bisect.bisect_left(self.preSum, x)
   