from typing import List


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        while low < len(nums) and high >= 0 and low <= high:
            mid = int((low + high) / 2)
            if nums[mid] == target:
                start = mid
                stop = mid
                while start >= 0 and nums[start] == target:
                    start -= 1
                start += 1

                while stop < len(nums) and nums[stop] == target:
                    stop += 1
                stop -= 1

                return [start, stop]
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1]


s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))
print(s.searchRange([5,7,7,8,8,10], 6))
print(s.searchRange([5,7,7,8,8,10], 5))
print(s.searchRange([5,7,7,8,8,10], 10))
print(s.searchRange([5,7,7,8,8,10], 7))
print(s.searchRange([5,7,7,8,8,10], 287))

