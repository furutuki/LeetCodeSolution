class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == val:
                nums[i] = nums[length-1]
                length -=1
            else:
                i += 1
        return length


s = Solution()
a = [0,1,2,2,3,0,4,2]
s.removeElement(a, 2)
print(a)

b = [3, 2, 2, 3]
s.removeElement(b, 3)
print(b)

c = [3, 2, 2, 3]
s.removeElement(c, 2)
print(c)


