import random
from typing import List


class Solution:

    def partition(self, nums: List[int], low: int, high: int):
        if low == high:
            return low

        index = random.randint(low, high)
        pivot = nums[index]
        i = low
        j = high - 1
        nums[index], nums[high] = nums[high], nums[index]
        while i <= j:
            while nums[i] <= pivot and i <= j:
                i += 1
            while nums[j] >= pivot and i <= j:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[high] = nums[high], nums[i]
        return i

    def quick_sort(self, nums: List[int], low: int, high: int):
        if low > high:
            return

        mid = self.partition(nums, low, high)
        self.quick_sort(nums, low, mid - 1)
        self.quick_sort(nums, mid + 1, high)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums[len(nums) - k]


s = Solution()
print(s.findKthLargest([3,1,2,4], 2))
# print(s.findKthLargest([3,2,1], 2))
# print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
# print(s.findKthLargest([3,2,1,5,6,4], 2))