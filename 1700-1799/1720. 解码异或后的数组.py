from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for num in encoded:
            arr.append(arr[-1] ^ num)
        return arr


so = Solution()
print(so.decode(encoded=[1, 2, 3], first=1))
