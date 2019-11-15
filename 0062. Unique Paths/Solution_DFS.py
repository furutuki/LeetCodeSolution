class Solution:

    cnt = 0

    def uniquePaths(self, m: int, n: int) -> int:

        self.cnt = 0

        def dfs(row: int, col: int):
            if row == n - 1 and col == m - 1:
                self.cnt += 1
                return

            if col < m - 1:
                dfs(row, col + 1)
            if row < n - 1:
                dfs(row + 1, col)

        dfs(0,0)
        return self.cnt


s = Solution()
print(s.uniquePaths(23, 8))
