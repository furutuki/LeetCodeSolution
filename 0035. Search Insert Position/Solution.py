from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] < target:
                pass
            elif nums[i] == target:
                return i
            else:
                return 0 if i == 0 else i
        return len(nums)


s = Solution()
print(s.searchInsert([1,3,5,6], 5))
print(s.searchInsert([1,3,5,6], 2))
print(s.searchInsert([1,3,5,6], 7))
print(s.searchInsert([1,3,5,6], 0))