from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        sum = nums[0]
        m = n = 0
        length = len(nums) + 1
        while m < len(nums) and n < len(nums):
            while sum < s:
                n += 1
                if n >= len(nums):
                    break
                else:
                    sum += nums[n]
            if sum >= s:
                if length > n - m + 1:
                    length = n - m + 1

            while sum >= s and m <= n:
                sum -= nums[m]
                m += 1
                if sum >= s:
                    if length > n - m + 1:
                        length = n - m + 1
                else:
                    break

        if length == len(nums) + 1:
            return 0
        else:
            return length


s = Solution()
print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(s.minSubArrayLen(100, []))
