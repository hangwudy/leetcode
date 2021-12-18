from collections import Counter
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        cnt = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        return min((word for word in words if not cnt - Counter(word)), key=len)
