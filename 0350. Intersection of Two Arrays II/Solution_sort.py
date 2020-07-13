from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        res = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                m = n = 1
                val = nums1[i]
                i += 1
                j += 1
                while i < len(nums1) and nums1[i] == nums1[i - 1]:
                    m += 1
                    i += 1
                while j < len(nums2) and nums2[j] == nums2[j - 1]:
                    n += 1
                    j += 1
                res.extend([val] * min(m, n))

        return res

s = Solution()
# print(s.intersect([1,2,2,1], [2,2]))
print(s.intersect([4,9,5], [9,4,9,8,4]))