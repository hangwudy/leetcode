from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        HEIGHT = 30
        seen = set()
        x = 0
        for k in range(HEIGHT, -1, -1):
            for num in nums:
                seen.add(num >> k)
            x_next = x * 2 + 1
            found = False
            for num in nums:
                if x_next ^ (num >> k) in seen:
                    found = True
                    break
            if found:
                x = x_next
            else:
                x = x_next - 1
        return x
