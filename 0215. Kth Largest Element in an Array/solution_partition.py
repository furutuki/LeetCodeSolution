from typing import List


class Solution:
    def partition(self, nums: List[int], low: int, high: int) -> int:
        m, n = low + 1, high
        while True:
            while nums[m] < nums[low] and m < high:
                m += 1
            while nums[n] > nums[low]:
                n -= 1
            if m < n:
                nums[m], nums[n] = nums[n], nums[m]
                m += 1
                n -= 1
            else:
                break
        nums[low], nums[n] = nums[n], nums[low]
        return n

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        low, high = 0, len(nums) - 1
        while low < high:
            p = self.partition(nums, low, high)
            if p == k:
                return nums[p]
            elif p > k:
                high = p - 1
            else:
                low = p + 1
        return nums[low]

s = Solution()
print(s.findKthLargest([3,3,3,3,3,3,3,3,3], 1))
print(s.findKthLargest([3,2,1,5,6,4], 2))
# print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))