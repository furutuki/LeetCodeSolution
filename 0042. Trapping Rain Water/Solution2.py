from typing import List


class Solution:

    def trap(self, height: List[int]) -> int:
        maxleft = 0
        maxright = 0
        left = 0
        right = len(height) - 1
        sum = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= maxleft:
                    maxleft = height[left]
                else:
                    sum += maxleft - height[left]
                left += 1
            else:
                if height[right] >= maxright:
                    maxright = height[right]
                else:
                    sum += maxright - height[right]
                right -= 1
        return sum