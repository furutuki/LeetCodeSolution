class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # for item in nums:
        #     if item == val:
        #         nums.remove(item)
        while val in nums:
            nums.remove(val)

        return len(nums)


s = Solution()
# a = [0,1,2,2,3,0,4,2]
# s.removeElement(a, 2)
# print(a)
#
# b = [3, 2, 2, 3]
# s.removeElement(b, 3)
# print(b)

c = [3, 2, 2, 3]
s.removeElement(c, 2)
print(c)


