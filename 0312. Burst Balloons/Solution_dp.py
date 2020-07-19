from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)

        points = [1 for i in range(n + 2)]
        for i in range(1, n + 1):
            points[i] = nums[i - 1]

        dp = [[0 for i in range(n + 2)] for _ in range(n + 2)]

        for i in range(n, -1, -1):
            for j in range(i + 1, n + 2):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][k] + dp[k][j] + points[i] * points[k] * points[j], dp[i][j])

        return dp[0][n + 1]


s = Solution()
print(s.maxCoins([3,1,5,8]))
