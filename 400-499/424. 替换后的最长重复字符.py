class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = maxn = 0
        nums = [0] * 26
        n = len(s)
        a_ord = ord("A")
        while right < n:
            nums[ord(s[right]) - a_ord] += 1
            maxn = max(maxn, nums[ord(s[right]) - a_ord])
            if right - left + 1 - maxn > k:
                nums[ord(s[left]) - a_ord] -= 1
                left += 1
            right += 1
        return right - left
