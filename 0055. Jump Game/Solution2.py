from typing import List

class Solution:

    def canJump(self, nums: List[int]) -> bool:
        """
        DP: dp[i] means whether the last item is reachable from index i
        """
        dp = [False] * len(nums)
        dp[len(nums) - 1] = True

        for i in range(len(nums) - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j < len(nums) and dp[i + j]:
                    dp[i] = True
                    break
        return dp[0]

s = Solution()
print(s.canJump([0]))
print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))
