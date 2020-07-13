from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = dict()
        for num in nums1:
            if d.__contains__(num):
                d[num] += 1
            else:
                d[num] = 1

        d2 = dict()
        for num in nums2:
            if d2.__contains__(num):
                d2[num] += 1
            else:
                d2[num] = 1

        res = []
        for k in d.keys():
            if d2.__contains__(k) and d2[k] > 0:
                min_value = min(d[k], d2[k])
                res.extend([k] * min_value)

        return res

s = Solution()
print(s.intersect([1,2,2,1], [2,2]))
print(s.intersect([4,9,5], [9,4,9,8,4]))