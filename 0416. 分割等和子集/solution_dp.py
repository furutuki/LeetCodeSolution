from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        "dp[i][j] 【0，i】区间是否能找到若干数字和为j"
        dp = [[False for col in range(target + 1)] for row in range(len(nums))]

        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(len(nums)):
            for j in range(target + 1):
                if nums[i] < j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                elif nums[i] == j:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][target]
