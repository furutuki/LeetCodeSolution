from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        f = [False for i in range(100001)]
        for num in nums:
            if f[num]:
                return num
            else:
                f[num] = True
