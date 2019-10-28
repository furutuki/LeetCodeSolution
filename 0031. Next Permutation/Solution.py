from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return nums

        for i in range(len(nums) - 1, -1, -1):
            if i == 0:
                self.reverse(nums)
            else:
                if nums[i - 1] < nums[i]:
                    for j in range(len(nums) - 1, i - 1, -1):
                        if nums[i - 1] < nums[j]:
                            self.swap(nums, i - 1, j)
                            self.section_sort(nums, i, len(nums) - 1)
                            return nums
                    break

        return nums

    def swap(self, nums: List[int], i: int, j: int):
        nums[i], nums[j] = nums[j], nums[i]

    def section_sort(self, nums: List[int], start: int, stop: int):
        for i in range(start, stop + 1):
            for j in range(i + 1, stop + 1):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

    def reverse(self, nums: List[int]):
        """
        reverse list
        """
        for i in range(int(len(nums) / 2)):
            nums[i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[i]


s = Solution()
print(s.nextPermutation([2, 3, 1]))
print(s.nextPermutation([1, 3, 2]))
print(s.nextPermutation([1, 2, 3]))
print(s.nextPermutation([3, 2, 1]))
print(s.nextPermutation([1, 1, 5]))
print(s.nextPermutation([1]))

