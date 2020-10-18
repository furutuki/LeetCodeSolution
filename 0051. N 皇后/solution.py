from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def backtrack(self, board: List[List[bool]], row: int):
        r = len(board)
        c = len(board[0])
        if row == r:
            solution = list()
            for i in range(r):
                rowdata = ""
                for j in range(c):
                    rowdata += 'Q' if board[i][j] else '.'
                solution.append(rowdata)
            self.ans.append(solution)
            return

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

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans = []
        board = [[False for r in range(n)] for c in range(n)]
        self.backtrack(board, 0)
        return self.ans
