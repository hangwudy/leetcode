from typing import List


class Trie:
    def __init__(self):
        self.L = 30
        self.left = None
        self.right = None

    def insert(self, val: int):
        node = self
        for i in range(self.L, -1, -1):
            bit = (val >> i) & 1
            if bit == 0:
                if not node.left:
                    node.left = Trie()
                node = node.left
            else:
                if not node.right:
                    node.right = Trie()
                node = node.right

    def get_max_xor(self, val: int) -> int:
        ans, node = 0, self
        for i in range(self.L, -1, -1):
            bit = (val >> i) & 1
            check = False
            if bit == 0:
                if node.right:
                    node = node.right
                    check = True
                else:
                    node = node.left
            else:
                if node.left:
                    node = node.left
                    check = True
                else:
                    node = node.right
            if check:
                ans |= 1 << i
        return ans


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n, q = len(nums), len(queries),
        nums.sort()
        queries = [(x, m, i) for i, (x, m) in enumerate(queries)]
        queries.sort(key=lambda query: query[1])

        ans = [0] * q
        t = Trie()
        idx = 0
        for x, m, qid in queries:
            while idx < n and nums[idx] <= m:
                t.insert(nums[idx])
                idx += 1
            if idx == 0:
                ans[qid] = -1
            else:
                ans[qid] = t.get_max_xor(x)
        return ans
