from typing import List


class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = list()
        min_diff = 1 << 32 - 1

        for x in range(len(nums) - 2):

            if x > 0 and nums[x] == nums[x - 1]:
                continue

            cur_num = nums[x]
            low = x + 1
            high = len(nums) - 1

            while low < high:

                total = nums[low] + nums[high] + cur_num
                diff = abs(total - target)

                if total > target:
                    if diff < min_diff:
                        min_diff = diff
                        result = [cur_num, nums[low], nums[high]]
                    high -= 1

                elif total < target:
                    if diff < min_diff:
                        min_diff = diff
                        result = [cur_num, nums[low], nums[high]]
                    low += 1

                else:
                    return total

        return sum(result)


s = Solution()
print(s.threeSumClosest([-1, 2, 1, -4], 1))
