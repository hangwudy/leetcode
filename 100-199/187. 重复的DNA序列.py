from collections import defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        dd = defaultdict(int)
        res = []
        for i in range(len(s) - L + 1):
            sub = s[i:i + L]
            dd[sub] += 1
            if dd[sub] == 2:
                res.append(sub)
        return res


so = Solution()
print(so.findRepeatedDnaSequences(s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
