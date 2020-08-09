from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def search(self, martix: List[List[int]], rowTop: int, rowBottom: int, colLeft: int, colRight: int, direction: int):
        if rowTop > rowBottom or colLeft > colRight:
            return

        if rowTop == rowBottom and colLeft == colRight:
            self.ans.append(martix[rowTop][colLeft])
            return

        #往右
        if direction == 0:
            for col in range(colLeft, colRight + 1):
                self.ans.append(martix[rowTop][col])
            self.search(martix, rowTop + 1, rowBottom, colLeft, colRight, 1)
        #往下
        elif direction == 1:
            for row in range(rowTop, rowBottom + 1):
                self.ans.append(martix[row][colRight])
            self.search(martix, rowTop, rowBottom, colLeft, colRight - 1, 2)
        #往左
        elif direction == 2:
            for col in range(colRight, colLeft - 1, -1):
                self.ans.append(martix[rowBottom][col])
            self.search(martix, rowTop , rowBottom - 1, colLeft, colRight, 3)
        #往上
        elif direction == 3:
            for row in range(rowBottom, rowTop - 1, -1):
                self.ans.append(martix[row][colLeft])
            self.search(martix, rowTop, rowBottom, colLeft + 1, colRight, 0)

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        self.ans = []
        row = len(matrix)
        col = len(matrix[0])
        self.search(matrix, 0, row - 1, 0, col - 1, 0)
        return self.ans