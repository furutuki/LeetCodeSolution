class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    for d in dir:
                        m = row + d[0]
                        n = col + d[1]
                        if 0 <= m < len(grid) and 0 <= n < len(grid[0]):
                            if grid[m][n] == 0:
                                ans += 1
                        else:
                            ans += 1
        return ans
