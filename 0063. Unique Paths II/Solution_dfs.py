from typing import List


class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[n - 1][m - 1] == 1:
            return 0

        mem = [[-1 for i in range(m)] for j in range(n)]

        def dfs(row: int, col: int):
            if row == n - 1 and col == m - 1:
                return 1 if obstacleGrid[row][col] == 0 else 0

            if mem[row][col] != -1:
                return mem[row][col]

            total = 0

            if row < n - 1 and obstacleGrid[row + 1][col] == 0:
                total += dfs(row + 1, col)
            if col < m - 1 and obstacleGrid[row][col + 1] == 0:
                total += dfs(row, col + 1)

            mem[row][col] = total

            return total

        return dfs(0,0)

    # Time Limit Exceeded solution
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #
    #     self.cnt = 0
    #     n = len(obstacleGrid)
    #     m = len(obstacleGrid[0])
    #
    #     def dfs(row: int, col: int):
    #         if obstacleGrid[row][col] == 1:
    #             return
    #
    #         if row == n - 1 and col == m - 1:
    #             self.cnt += 1
    #             return
    #
    #         if col < m - 1:
    #             dfs(row, col + 1)
    #         if row < n - 1:
    #             dfs(row + 1, col)
    #
    #     dfs(0,0)
    #     return self.cnt


s = Solution()
print(s.uniquePathsWithObstacles(
[[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]
))
# print(s.uniquePathsWithObstacles([[1,0]]))
# print(s.uniquePathsWithObstacles([
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]))
