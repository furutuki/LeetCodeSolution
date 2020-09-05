from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m, n = 0, len(nums) - 1
        t = nums[m] + nums[n]
        while t != target and m < n:
            if t > target:
                mid = (m + n) // 2
                p = nums[m] + nums[mid]
                if p > target:
                    n = mid - 1
                elif p < target:
                    n -= 1
                else:
                    return [nums[m], nums[mid]]
            elif t < target:
                mid = (m + n) // 2
                q = nums[mid] + nums[n]
                if q < target:
                    m = mid + 1
                elif q > target:
                    m += 1
                else:
                    return [nums[mid], nums[n]]
            else:
                return [nums[m], nums[n]]

            t = nums[m] + nums[n]

        return [nums[m], nums[n]]

s = Solution()
print(s.twoSum([18,19,25,30,39,41,61,77,88,97], 59))