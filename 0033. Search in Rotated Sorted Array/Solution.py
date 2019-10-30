from typing import List


class Solution:

    def divide_and_conquer(self, nums, low, high, target):
        if low > high:
            return -1

        mid = int((low + high) / 2)
        if nums[mid] == target:
            return mid

        if low <= mid - 1 and nums[low] <= nums[mid - 1]:
            if nums[low] <= target <= nums[mid - 1]:
                return self.divide_and_conquer(nums, low, mid - 1, target)
            else:
                return self.divide_and_conquer(nums, mid + 1, high, target)

        elif mid + 1 <= high and nums[mid + 1] <= nums[high]:
            if nums[mid + 1] <= target <= nums[high]:
                return self.divide_and_conquer(nums, mid + 1, high, target)
            else:
                return self.divide_and_conquer(nums, low, mid - 1, target)

        else:
            return -1

    def search(self, nums: List[int], target: int) -> int:
        return self.divide_and_conquer(nums, 0, len(nums) - 1, target)


s = Solution()
print(s.search([4,5,6,7,0,1,2], 0))
print(s.search([4,5,6,7,0,1,2], 3))
print(s.search([6,7,1,2,3,4,5], 6))
print(s.search([3,4,5,6,1,2], 2))


