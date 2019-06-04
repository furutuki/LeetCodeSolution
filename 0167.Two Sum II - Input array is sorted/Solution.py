class Solution:
    def twoSum(self, nums: 'List[int]', target: int) -> 'List[int]':
        start = 0
        end = len(nums) - 1
        res = []
        while start < end :
            if nums[start] + nums[end] > target:
                end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                res.append(start + 1)
                res.append(end + 1)
                return res



s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
