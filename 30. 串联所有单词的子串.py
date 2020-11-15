from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        n = len(s)
        one_word = len(words[0])
        n_word = one_word * len(words)
        target = Counter(words)
        ans = []
        for i in range(0, n - n_word + 1):
            tmp = s[i:i + n_word]
            c_tmp = []
            for j in range(0, n_word, one_word):
                c_tmp.append(tmp[j:j + one_word])
            if Counter(c_tmp) == target:
                ans.append(i)
        return ans
