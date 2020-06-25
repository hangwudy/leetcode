from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(comb, next_digit):
            if not next_digit:
                res.append(comb)
            else:

                for i in phone[next_digit[0]]:
                    # comb += i
                    backtrack(comb + i, next_digit[1:])

        res = []
        if digits:
            backtrack("", digits)
        return res


so = Solution()
print(so.letterCombinations("23"))
