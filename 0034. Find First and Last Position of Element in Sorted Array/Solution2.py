from typing import List


class Solution2:

    def binary_search(self, low: int, high: int, nums: List[int], target: int) -> List[int]:
        if low > high:
            return [-1, -1]

        if nums[low] == target == nums[high]:
            return [low, high]

        if nums[low] <= target <= nums[high]:
            mid = int((low + high) / 2)
            l, r = [self.binary_search(low, mid, nums, target), self.binary_search(mid + 1, high, nums, target)]
            if -1 in l + r:
                return max(l, r)
            else:
                return [l[0], r[1]]

        return [-1, -1]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.binary_search(0, len(nums) - 1, nums, target)


s = Solution2()
print(s.searchRange([5,7,7,8,8,10], 8))
print(s.searchRange([5,7,7,8,8,10], 6))
print(s.searchRange([5,7,7,8,8,10], 5))
print(s.searchRange([5,7,7,8,8,10], 10))
print(s.searchRange([5,7,7,8,8,10], 7))
print(s.searchRange([5,7,7,8,8,10], 287))
print(s.searchRange([], 0))



