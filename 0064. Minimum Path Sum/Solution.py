from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """ row count """
        n = len(grid)

        """ col count """
        m = len(grid[0])

        """initialize a n * m array"""
        min_step = [[0 for col in range(m)] for row in range(n)]

        """ init all item in last row to 1"""
        min_step[n - 1][m - 1] = grid[n - 1][m - 1]
        for col in range(m - 2, -1, -1):
            min_step[n - 1][col] = grid[n - 1][col] + min_step[n - 1][col + 1]

        """ init all item in last col to 1"""
        for row in range(n - 2, -1, -1):
            min_step[row][m - 1] = grid[row][m - 1] + min_step[row + 1][m - 1]

        for row in range(n - 2, -1, -1):
            for col in range(m - 2, -1, -1):
                min_step[row][col] = min(min_step[row][col + 1], min_step[row + 1][col]) + grid[row][col]

        return min_step[0][0]


s = Solution()
print(s.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))