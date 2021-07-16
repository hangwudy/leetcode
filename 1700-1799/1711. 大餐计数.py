from typing import List
from collections import defaultdict


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        maxsum = max(deliciousness) * 2
        pairs = 0
        dd = defaultdict(int)
        for i in deliciousness:
            s = 1
            while s <= maxsum:
                count = dd[s - i]
                pairs += count
                s <<= 1
            dd[s - i] += 1
        return pairs % 1000000007
