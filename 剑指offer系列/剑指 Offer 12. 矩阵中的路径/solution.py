from typing import List


class Solution:

    def dfs(self, board: List[List[str]], i: int, j: int, k: int, word: str) -> bool:
        row = len(board)
        col = len(board[0])

        if i < 0 or i >= row or j < 0 or j >= col or board[i][j] != word[k]:
            return False

        if k == len(word) - 1:
            return True

        tmp = board[i][j]
        board[i][j] = '*'

        sub_res = self.dfs(board, i + 1, j, k + 1, word) or self.dfs(board, i - 1, j, k + 1, word) \
                  or self.dfs(board, i, j + 1, k + 1, word) or self.dfs(board, i, j - 1, k + 1, word)

        board[i][j] = tmp

        return sub_res

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, 0, word):
                    return True
        return False
