from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        def set_flag() -> None:
            for i in range(9):
                for j in range(9):
                    if board[i][j] != '.':
                        val = int(board[i][j])
                        row_used[i][val] = True
                        col_used[j][val] = True
                        box_used[int(i / 3) * 3 + int(j / 3)][val] = True

        def can_place(num: int, row: int, col: int):
            return not row_used[row][num] and not col_used[col][num] and not box_used[int(row / 3) * 3 + int(col / 3)][num]

        def back_track(row: int, col: int):
            if col == 9:
                col = 0
                row += 1
                if row == 9:
                    return True

            if board[row][col] == '.':
                for num in range(1, 10):
                    can_placed = can_place(num, row, col)

                    if can_placed:
                        board[row][col] = str(num)
                        row_used[row][num] = True
                        col_used[col][num] = True
                        box_used[int(row / 3) * 3 + int(col / 3)][num] = True
                        if back_track(row, col + 1):
                            return True
                        board[row][col] = '.'
                        row_used[row][num] = False
                        col_used[col][num] = False
                        box_used[int(row / 3) * 3 + int(col / 3)][num] = False
            else:
                return back_track(row, col + 1)

        row_used = [{j: False for j in range(1, 10)} for i in range(9)]
        col_used = [{j: False for j in range(1, 10)} for i in range(9)]
        box_used = [{j: False for j in range(1, 10)} for i in range(9)]

        set_flag()
        back_track(0, 0)


s = Solution()
a = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
s.solveSudoku(a)
print(a)
