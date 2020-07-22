from typing import List


class Solution:

    def dfs(self, visited: List[List[bool]], i: int, j: int, m: int, n: int, k: int) -> int:
        if i < 0 or i >= m or j < 0 or j >= n or (i // 10 + i % 10 + j // 10 + j % 10) > k or visited[i][j]:
            return 0

        visited[i][j] = True

        total = self.dfs(visited, i + 1, j, m, n, k) + self.dfs(visited, i - 1, j, m, n, k) \
                + self.dfs(visited, i, j + 1, m, n, k) + self.dfs(visited, i, j - 1, m, n, k)

        return total + 1

    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = [[False for col in range(n)] for row in range(m)]
        return self.dfs(visited, 0, 0, m, n, k)
