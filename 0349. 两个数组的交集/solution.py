from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set()
        ans = set()
        for item in nums1:
            s.add(item)
        for item in nums2:
            if item in s:
                ans.add(item)
        return list(ans)
print(Solution().intersection([1,2,2,1],[2,2]))