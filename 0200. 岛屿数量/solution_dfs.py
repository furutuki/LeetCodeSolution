from typing import List


class Solution:

    def __init__(self):
        self.ans = 0

    def dfs(self, m: int, n: int, i: int, j: int, grid: List[List[str]], flag: List[List[bool]]):
        flag[i][j] = True
        if i - 1 >= 0 and not flag[i - 1][j] and grid[i - 1][j] == '1':
            self.dfs(m, n, i - 1, j, grid, flag)
        if i + 1 < m and not flag[i + 1][j] and grid[i + 1][j] == '1':
            self.dfs(m, n, i + 1, j, grid, flag)
        if j - 1 >= 0 and not flag[i][j - 1] and grid[i][j - 1] == '1':
            self.dfs(m, n, i, j - 1, grid, flag)
        if j + 1 < n and not flag[i][j + 1] and grid[i][j + 1] == '1':
            self.dfs(m, n, i, j + 1, grid, flag)

    def solve(self, m: int, n: int,  grid: List[List[str]], flag: List[List[bool]]):
        for i in range(m):
            for j in range(n):
                if not flag[i][j] and grid[i][j] == '1':
                    self.dfs(m, n, i, j, grid, flag)
                    self.ans += 1

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        flag = [[False for col in range(n)] for row in range(m)]

        self.ans = 0
        self.solve(m, n, grid, flag)
        return self.ans


