from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]):
        if len(nums) < 2:
            return nums

        for i in range(len(nums) - 1, -1, -1):
            if i == 0:
                nums.reverse()
            else:
                if nums[i - 1] < nums[i]:
                    for j in range(len(nums) - 1, i - 1, -1):
                        if nums[i - 1] < nums[j]:
                            nums[i - 1], nums[j] = nums[j], nums[i - 1]
                            nums[i:] = sorted(nums[i:])
                            return nums
        return nums

s = Solution()
print(s.nextPermutation([2, 3, 1]))
print(s.nextPermutation([1, 3, 2]))
print(s.nextPermutation([1, 2, 3]))
print(s.nextPermutation([3, 2, 1]))
print(s.nextPermutation([1, 1, 5]))
print(s.nextPermutation([1]))

