from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        length = len(matrix)

        for i in range(length):
            for j in range(i, length - 1 - i):
                # tmp = matrix[j][length - i]
                # matrix[j][length - i] = matrix[i][j]
                tmp = matrix[i][j]
                matrix[i][j] = matrix[length - 1 - j][i]
                matrix[length - 1 - j][i] = matrix[length - 1 - i][length - 1 - j]
                matrix[length - 1 - i][length - 1 - j] = matrix[j][length - 1 - i]
                matrix[j][length - 1 - i] = tmp
        return matrix

s = Solution()
print(s.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
]))

