from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_len = len(s)
        t_len = len(t)
        begin = 0
        win_freq = {}
        t_freq = dict(Counter(t))

        min_len = s_len + 1
        distance = 0
        left = 0
        right = 0
        while right < s_len:
            if s[right] in t_freq and t_freq[s[right]] == 0:
                right += 1
                continue
            win_freq.setdefault(s[right], 0)
            if s[right] in t_freq and win_freq[s[right]] < t_freq[s[right]]:
                distance += 1
            win_freq[s[right]] += 1
            right += 1

            # 满足条件时，进行左边缘移动
            while distance == t_len:
                # win_freq.setdefault(s[left], 0)
                if right - left < min_len:
                    min_len = right - left
                    begin = left
                if s[left] not in t_freq:
                    left += 1
                    continue
                if s[left] in t_freq and win_freq[s[left]] == t_freq[s[left]]:
                    distance -= 1
                win_freq[s[left]] -= 1
                left += 1

        if min_len == s_len + 1:
            return ""

        return s[begin:begin + min_len]


so = Solution()
print(so.minWindow(s="ADOBECODEBANC", t="ABC"))
