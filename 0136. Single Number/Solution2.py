class Solution(object):
    def singleNumber(self, nums):
        return sum(list(set(nums)))*2 - sum(nums)


s = Solution()
print(s.singleNumber([2,2,1]))
print(s.singleNumber([4,1,2,1,2]))