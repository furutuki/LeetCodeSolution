from typing import List


class Solution:

    def partition(self, nums: List[int], low: int, high: int):
        stub = nums[low]
        while low < high:
            while nums[high] >= stub and low < high:
                high -= 1
            nums[low] = nums[high]
            while nums[low] <= stub and low < high:
                low += 1
            nums[high] = nums[low]
        nums[low] = stub
        return low

    def quick_sort(self, nums: List[int], low: int, high: int):
        if low > high:
            return

        mid = self.partition(nums, low, high)
        self.quick_sort(nums, low, mid - 1)
        self.quick_sort(nums, mid + 1, high)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums[len(nums) - k]

