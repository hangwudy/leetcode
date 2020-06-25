from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        return [int(i) for i in str(num + 1)]


so = Solution()
print(so.plusOne([1, 2, 3]))
