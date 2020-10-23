from typing import List
from collections import deque

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        ans = 0
        flag = [[False for col in range(n)] for row in range(m)]

        for row in range(m):
            for col in range(n):
                if not flag[row][col] and grid[row][col] == '1':
                    flag[row][col] = True
                    queue.append(row * n + col)
                    while queue:
                        num = queue.popleft()
                        i = num // n
                        j = num % n
                        if i - 1 >= 0 and not flag[i - 1][j] and grid[i - 1][j] == '1':
                            queue.append((i - 1) * n + j)
                            flag[i - 1][j] = True
                        if i + 1 < m and not flag[i + 1][j] and grid[i + 1][j] == '1':
                            queue.append((i + 1) * n + j)
                            flag[i + 1][j] = True
                        if j - 1 >= 0 and not flag[i][j - 1] and grid[i][j - 1] == '1':
                            queue.append(i * n + j - 1)
                            flag[i][j - 1] = True
                        if j + 1 < n and not flag[i][j + 1] and grid[i][j + 1] == '1':
                            queue.append(i * n + j + 1)
                            flag[i][j + 1] = True
                    ans += 1
        return ans

