from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        N = len(nums)

        dp = [[0, 0] for i in range(N)]
        dp[0][0] = 0
        dp[0][1] = nums[0]

        for i in range(1, N):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]

        return max(dp[N - 1][0], dp[N - 1][1])