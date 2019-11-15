class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        """initialize a n * m array"""
        paths = [[0 for col in range(m)] for row in range(n)]

        """ init all item in last row to 1"""
        for col in range(m):
            paths[n - 1][col] = 1

        """ init all item in last col to 1"""
        for row in range(n):
            paths[row][m - 1] = 1

        for row in range(n - 2, -1, -1):
            for col in range(m - 2, -1, -1):
                paths[row][col] = paths[row][col + 1] + paths[row + 1][col]

        return paths[0][0]


s = Solution()
print(s.uniquePaths(23, 18))
