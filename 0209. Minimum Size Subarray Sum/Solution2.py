from typing import List

"比Solution.py改进了，代码更简洁快速的滑动窗口算法"
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = right = sum = 0
        length = len(nums) + 1
        while right < len(nums):
            sum += nums[right]
            right += 1
            while sum >= s:
                length = min(length, right - left)
                sum -= nums[left]
                left += 1
        return 0 if length == len(nums) + 1 else length


s = Solution()
print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(s.minSubArrayLen(100, []))
