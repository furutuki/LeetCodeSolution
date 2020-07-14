from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = col = len(triangle)

        dp = [[0 for i in range(col)] for _ in range(row)]
        dp[0][0] = triangle[0][0]
        if row > 1:
            for r in range(1, row):
                dp[r][0] = dp[r - 1][0] + triangle[r][0]
                dp[r][r] = dp[r - 1][r- 1] + triangle[r][r]

            for r in range(1, row):
                for c in range(1, r):
                    dp[r][c] = min(dp[r - 1][c], dp[r - 1][c - 1]) + triangle[r][c]

        min_value = dp[row - 1][0]
        for c in range(1, col):
            min_value = min(min_value, dp[row - 1][c])

        return min_value


arr = [
     [2],
     [3,4],
     [6,5,7],
     [4,1,8,3]
]
s = Solution()
print(s.minimumTotal(arr))

