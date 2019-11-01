from typing import List


class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        mapping_list = [{},{},{},{},{},{},{},{},{}]

        for i in range(9):
            line = board[i]
            mapping = {}
            mapping2 = {}

            for j in range(9):
                if line[j] != ".":
                    if mapping.get(line[j]):
                        return False
                    else:
                        mapping[line[j]] = 1

                if board[j][i] != ".":
                    if mapping2.get(board[j][i]):
                        return False
                    else:
                        mapping2[board[j][i]] = 1

                box_index = int(i / 3) * 3 + int(j / 3)
                if board[i][j] != ".":
                    if mapping_list[box_index].get(board[i][j]):
                        return False
                    else:
                        mapping_list[box_index][board[i][j]] = 1

        return True

# t = [{}] * 4
# t[2]["hello"] = "s"
# print(t)
#
# t = [{},{},{},{}]
# t[2]["hello"] = "s"
# print(t)

