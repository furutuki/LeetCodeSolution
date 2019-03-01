class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        matrix = [[0 for x in range(0, len(nums))] for y in range(0, len(nums))]
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                matrix[i][j] = nums[i] + nums[j]
        res = list()



s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))