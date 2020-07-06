from typing import List


class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        """initialize a n * m array"""
        paths = [[0 for col in range(m)] for row in range(n)]

        if obstacleGrid[0][0] == 1:
            return 0

        if obstacleGrid[n - 1][m - 1] == 0:
            paths[n - 1][m - 1] = 1
        else:
            return 0

        """ init all item in last row to 1"""
        for col in range(m - 2, -1, -1):
            if obstacleGrid[n - 1][col] == 0:
                paths[n - 1][col] = 1
            else:
                break

        """ init all item in last col to 1"""
        for row in range(n - 2, -1, -1):
            if obstacleGrid[row][m - 1] == 0:
                paths[row][m - 1] = 1
            else:
                break

        for row in range(n - 2, -1, -1):
            for col in range(m - 2, -1, -1):
                paths[row][col] = paths[row][col + 1] + paths[row + 1][col] if obstacleGrid[row][col] == 0 else 0

        return paths[0][0]


s = Solution()
print(s.uniquePathsWithObstacles(
[[0,0],[1,0]]
))