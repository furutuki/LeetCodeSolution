from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        i, j = 0, len(nums) - 1
        while i < j and i < len(nums) and j >= 0:
            while i < len(nums) and nums[i] % 2 == 1:
                i += 1
            while j >= 0 and nums[j] % 2 == 0:
                j -= 1
            if i < j and i < len(nums) and j >= 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        return nums

s = Solution()
print(s.exchange([1,3,5]))