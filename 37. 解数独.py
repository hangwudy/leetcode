from collections import defaultdict
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = 3
        N = n ** 2
        box_index = lambda row, col: (row // n) * n + col // n

        rows = [defaultdict(int) for i in range(N)]
        cols = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]

        sudoku_solved = False

        def place_number(d, row, col):
            rows[row][d] += 1
            cols[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)

        def could_place(d, row, col):
            return not (d in rows[row] or d in cols[col] or d in boxes[box_index(row, col)])

        def remove_number(d, row, col):
            del rows[row][d]
            del cols[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = "."

        def place_next_numbers(row, col):
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            else:
                if col == N - 1:
                    return backtrack(row + 1, 0)
                else:
                    return backtrack(row, col + 1)
            return

        def backtrack(row, col):
            if board[row][col] == ".":
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)

                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)

        for i in range(N):
            for j in range(N):
                if board[i][j] != ".":
                    d = int(board[i][j])
                    place_number(d, i, j)

        backtrack(0, 0)


so = Solution()
sudoku = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", ".", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          [".", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

so.solveSudoku(sudoku)
for i in sudoku:
    print(i)
