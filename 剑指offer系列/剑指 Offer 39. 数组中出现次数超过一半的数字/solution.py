from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        max_cnt = 0
        ans = -1
        for item in nums:
            if d.__contains__(item):
                d[item] += 1
            else:
                d[item] = 1
            if d[item] > max_cnt:
                max_cnt = d[item]
                ans = item
        return ans
