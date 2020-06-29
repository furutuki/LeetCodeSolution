from typing import List


class Solution:

    def merge(self, nums: List[int], left: int, mid: int, right: int):
        i = left
        j = mid + 1
        res = []
        while i <= mid < j <= right:
            if nums[i] < nums[j]:
                res.append(nums[i])
                i += 1
            else:
                res.append(nums[j])
                j += 1
        if i <= mid:
            res.extend(nums[i:mid + 1])
        else:
            res.extend(nums[j : right + 1])

        for i in range(right - left + 1):
            nums[i + left] = res[i]

    def mergeSort(self, nums: List[int], left: int, right: int):
        if left >= right:
            return

        mid = (left + right) // 2
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums[len(nums) - k]


s = Solution()
print(s.findKthLargest([3,1,2,4], 2))
print(s.findKthLargest([3,2,1], 2))
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
print(s.findKthLargest([3,2,1,5,6,4], 2))
