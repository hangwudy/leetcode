from pprint import pprint
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r, c = len(board), len(board[0])
        rows = [[0] * 9 for _ in range(r)]
        col = [[0] * 9 for _ in range(c)]
        subbox = [[[0] * 9 for _ in range(3)] for __ in range(3)]
        pprint(rows)
        pprint(col)
        pprint(subbox)
        for i in range(r):
            for j in range(c):
                ch = board[i][j]
                if ch != ".":
                    index = ord(ch) - ord("0") - 1
                    rows[i][index] += 1
                    col[j][index] += 1
                    subbox[i // 3][j // 3][index] += 1
                    if rows[i][index] > 1 or col[j][index] > 1 or subbox[i // 3][j // 3][index] > 1:
                        return False
        return True


so = Solution()
print(so.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                           , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                           , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                           , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                           , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                           , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                           , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                           , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                           , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
