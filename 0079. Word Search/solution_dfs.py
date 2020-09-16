from typing import List


class Solution:
    def dfs(self, board: List[List[str]], word: str, row: int, col: int, step: int) -> bool:
        if len(board) > row >= 0 and len(board[0]) > col >= 0:
            if board[row][col] != word[step]:
                return False
            elif step == len(word) - 1:
                return True
        else:
            return False

        tmp = board[row][col]
        board[row][col] = '#'

        ans = self.dfs(board, word, row + 1, col, step + 1) or \
              self.dfs(board, word, row - 1, col, step + 1) or \
              self.dfs(board, word, row, col - 1, step + 1) or \
              self.dfs(board, word, row, col + 1, step + 1)

        board[row][col] = tmp
        return ans

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False


s = Solution()
print(s.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
