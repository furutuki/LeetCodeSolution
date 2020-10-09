from typing import List


class Solution:

    def __init__(self):
        self.ans = -1

    def maxValue(self, grid: List[List[int]]) -> int:
        self.ans = -1

        r = len(grid)
        c = len(grid[0])

        dp = [[0 for col in range(c)] for row in range(r)]
        dp[0][0] = grid[0][0]

        for col in range(1, c):
            dp[0][col] = dp[0][col - 1] + grid[0][col]

        for row in range(1, r):
            dp[row][0] = dp[row - 1][0] + grid[row][0]

        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] = max(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])

        return dp[r - 1][c - 1]

s = Solution()
print(s.maxValue([[1,2,5],[3,2,1]]))