from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row = len(matrix)
        col = len(matrix[0])

        if row == 0 or col == 0:
            return False

        r = 0
        c = col - 1
        while 0 <= r < row and 0 <= c < col:
            if target > matrix[r][c]:
                r += 1
            elif target < matrix[r][c]:
                c -= 1
            else:
                return True
        return False

s = Solution()
print(s.findNumberIn2DArray([[-5]], -10))