from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        index = 0
        while index <= right and left < right:
            if nums[index] == 2:
                if nums[right] != 2:
                    nums[index], nums[right] = nums[right], nums[index]
                right -= 1
            elif nums[index] == 0:
                if nums[left] != 0:
                    nums[left], nums[index] = nums[index], nums[left]
                left += 1
                if left > index:
                    index = left
            else:
                index += 1


s = Solution()
l = [0,2,1,1,0]
s.sortColors(l)
print(l)
