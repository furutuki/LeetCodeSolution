from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        dp[i]表示【0，i】区间内以i结尾的子列表的最大的和
        """

        max_sum = nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            max_sum = max(max_sum, dp[i])
        return max_sum

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4],))

