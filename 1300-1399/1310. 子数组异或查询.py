from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors = [0]
        for i in arr:
            xors.append(xors[-1] ^ i)

        ans = list()
        for left, right in queries:
            ans.append(xors[left] ^ xors[right + 1])
        return ans
