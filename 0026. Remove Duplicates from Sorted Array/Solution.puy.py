class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        prev = nums[0]

        for i in range(1, len(nums)):
            while i < len(nums) and nums[i] == prev:
                nums.remove(nums[i])
            if i >= len(nums):
                break
            else:
                prev = nums[i]
        return len(nums)


s = Solution()
nums = [1, 1]
length = s.removeDuplicates(nums)
print(length)
print(nums)

