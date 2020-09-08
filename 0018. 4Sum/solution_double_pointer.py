from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = list()

        for x in range(len(nums) - 3):
            if x > 0 and nums[x] == nums[x - 1]:
                continue

            for y in range(x + 1, len(nums) - 2):
                if y > x + 1 and nums[y] == nums[y - 1]:
                    continue

                pre_sum = nums[x] + nums[y]
                low = y + 1
                high = len(nums) - 1

                while low < high:

                    if nums[low] + nums[high] + pre_sum > target:
                        high -= 1

                    elif nums[low] + nums[high] + pre_sum < target:
                        low += 1

                    else:
                        result.append([nums[x], nums[y], nums[low], nums[high]])

                        while low + 1 < high and nums[low] == nums[low + 1]:
                            low += 1
                        while high - 1 > low and nums[high] == nums[high - 1]:
                            high -= 1

                        low += 1
                        high -= 1

        return result

s = Solution()
print(s.fourSum( [0,0,0,0], 1))