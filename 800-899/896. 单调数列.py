from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        if n <= 2:
            return True
        delta = 0
        for i in range(1, n):
            if A[i] != A[i - 1]:
                delta = A[i] - A[i - 1]
                break
        for i in range(2, n):
            if (A[i] - A[i - 1]) * delta < 0:
                return False
        return True


so = Solution()
print(so.isMonotonic([1, 2, 2, 3]))
print(so.isMonotonic([6, 5, 4, 4]))
print(so.isMonotonic([1, 3, 2]))
print(so.isMonotonic([2, 2, 2, 1, 4, 5]))
