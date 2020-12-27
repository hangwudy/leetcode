class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds = dict()
        dt = dict()
        m = len(s)
        n = len(t)
        if m != n:
            return False
        for i in range(m):
            if s[i] not in ds and t[i] not in dt:
                ds[s[i]] = t[i]
                dt[t[i]] = s[i]
            else:
                if ds.get(s[i]) != t[i] or dt.get(t[i]) != s[i]:
                    return False
        return True


so = Solution()
print(so.isIsomorphic(s="ab", t="aa"))
