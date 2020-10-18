from typing import List


class Solution:
    def __init__(self):
        self.ans = 0

    def backtrack(self, board: List[List[bool]], row: int):
        r = len(board)
        if row == r:
            self.ans += 1
            return
        c = len(board[0])
        for i in range(c):
            if self.isValid(row, i, board, c):
                board[row][i] = True
                self.backtrack(board, row + 1)
                board[row][i] = False

    def isValid(self, row: int, col: int, board: List[List[bool]], c: int) -> bool:
        for r in range(row):
            if board[r][col]:
                return False

        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j]:
                return False
            i -= 1
            j -= 1

        i, j = row - 1, col + 1
        while i >= 0 and j < c:
            if board[i][j]:
                return False
            i -= 1
            j += 1
        return True

    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        board = [[False for r in range(n)] for c in range(n)]
        self.backtrack(board, 0)
        return self.ans
