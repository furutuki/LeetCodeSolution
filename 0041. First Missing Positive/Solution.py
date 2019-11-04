from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums) and nums[i] <= 0:
            i += 1
            continue
        j = 1
        while i < len(nums):
            if nums[i] == j:
                i += 1
                if i == len(nums):
                    return j + 1
                elif nums[i - 1] < nums[i]:
                    j += 1
            else:
                break
        return j


s = Solution()
print(s.firstMissingPositive([0, 2, 2, 1, 1]))
print(s.firstMissingPositive([1, 2, 0]))
print(s.firstMissingPositive([3,4,-1, 1]))
print(s.firstMissingPositive([7,8,9,10,11]))

