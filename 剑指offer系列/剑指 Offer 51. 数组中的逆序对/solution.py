from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.ans = 0

        def merge(nums: List[int], start: int, mid: int, end: int, temp: List[int]):
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j +=1
                    self.ans += mid - i + 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= end:
                temp.append(nums[j])
                j += 1
            for i in range(len(temp)):
                nums[start + i] = temp[i]
            temp.clear()

        def mergeSort(nums: List[int], start: int, end: int, temp: List[int]):
            if start >= end:
                return
            mid = (start + end) // 2
            mergeSort(nums, start, mid, temp)
            mergeSort(nums, mid + 1, end, temp)
            merge(nums, start, mid, end, temp)

        mergeSort(nums, 0, len(nums) - 1, [])
        return self.ans

