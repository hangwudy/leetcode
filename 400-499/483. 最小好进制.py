class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)

        def check(x, m):
            res = 0
            for _ in range(m + 1):
                res = res * x + 1
            return res

        ans = float('inf')
        for i in range(1, 64):
            l = 2
            r = num
            while r > l:
                mid = l + (r - l) // 2
                tmp = check(mid, i)
                if tmp == num:
                    ans = min(ans, mid)
                    break
                elif tmp > num:
                    r = mid
                else:
                    l = mid + 1
        return str(ans)
