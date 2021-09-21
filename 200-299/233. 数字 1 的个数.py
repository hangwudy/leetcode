class Solution:
    def countDigitOne(self, n: int) -> int:
        k, mulk = 0, 1
        ans = 0
        while n >= mulk:
            ans += (n // (mulk * 10) * mulk + min(max(n % (mulk * 10) - mulk + 1, 0), mulk))
            k += 1
            mulk *= 10
        return ans
