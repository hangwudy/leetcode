class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        min_ = 0
        max_ = 0
        for c in s:
            if c == "(":
                min_ += 1
                max_ += 1
            elif c == ")":
                min_ = max(min_ - 1, 0)
                max_ -= 1
                if max_ < 0:
                    return False
            else:
                min_ = max(min_ - 1, 0)
                max_ += 1
        return min_ == 0
  