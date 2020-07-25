from typing import List


class Solution:

    def check(self, nums: List[int], target: int, m: int) -> bool:
        cnt, right = 1, 0
        for i in range(len(nums)):
            if right + nums[i] > target:
                cnt += 1
                right = nums[i]
            else:
                right += nums[i]
        return cnt <= m

    def splitArray(self, nums: List[int], m: int) -> int:
        """求出数组和以及元素最大值分别作为二分的上下限"""
        right = sum(nums)
        left = max(nums)

        while left < right:
            mid = (left + right) // 2
            if self.check(nums, mid, m):
                right = mid
            else:
                left = mid + 1
        return left

s = Solution()
print(s.splitArray([7,2,5,10,8], 2))