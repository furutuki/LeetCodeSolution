from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            if d.__contains__(num):
                return num
            else:
                d[num] = True
