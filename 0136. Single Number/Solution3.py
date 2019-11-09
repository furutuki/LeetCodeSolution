class Solution(object):
    def singleNumber(self, nums):
        res = 0
        for item in nums:
            res ^= item
        return res


s = Solution()
print(s.singleNumber([2,2,1]))
print(s.singleNumber([4,1,2,1,2]))