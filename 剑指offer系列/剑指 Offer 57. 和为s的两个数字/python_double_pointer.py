class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m, n = 0, len(nums) - 1
        t = nums[m] + nums[n]
        while t != target:
            if t > target:
                n -= 1
            else:
                m += 1
            t = nums[m] + nums[n]
        return [nums[m], nums[n]]
