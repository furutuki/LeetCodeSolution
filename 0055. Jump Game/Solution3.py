from typing import List

class Solution:

    def canJump(self, nums: List[int]) -> bool:
        """
        DP: dp[i] means whether nums[i] is reachable
        """
        dp = [False] * len(nums)
        dp[0] = True

        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if dp[j] and nums[j] + j >= i:
                    dp[i] = True
                    break
        return dp[len(nums) - 1]


s = Solution()
print(s.canJump([0]))
print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))
