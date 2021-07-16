from collections import defaultdict
import bisect


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dd = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dd[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        l = self.dd.get(key)
        if not l:
            return ""

        a = bisect.bisect_right(l, [timestamp, "z" * 101])
        if not a:
            return ""
        return l[a - 1][1]
