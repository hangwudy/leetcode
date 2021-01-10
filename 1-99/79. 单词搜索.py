from typing import List


class Solution:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.backtrack(board, word, i, j, 0, visited):
                    return True
        return False

    def backtrack(self, board, word, row, col, index, visited):
        if board[row][col] != word[index]:
            return False
        if index == len(word) - 1:
            return board[row][col] == word[index]
        visited[row][col] = True
        for p, q in self.directions:
            new_row = row + p
            new_col = col + q
            if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and not visited[new_row][new_col] and \
                    self.backtrack(board, word, new_row, new_col, index + 1, visited):
                return True

        visited[row][col] = False
        return False


so = Solution()
print(so.exist(board=
[
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
],
    word="ABCCED"))
