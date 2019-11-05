from typing import List


class Solution:

    def findBorder(self, height: List[int], start_index: int):
        height_len = len(height)
        if start_index >= height_len:
            return None
        for i in range(start_index, height_len - 1):
            if height[i] > height[i + 1]:
                return i
        if height[height_len - 1] >= height[height_len - 2]:
            return height_len - 1

    def findRightBorder(self, height: List[int], start_index: int, left_border_val: int):
        if start_index >= len(height):
            return None

        if height[start_index] >= left_border_val:
            return start_index

        max_index = start_index - 1
        max_height = height[max_index]
        height_len = len(height)

        for i in range(start_index, height_len):
            if height[i] > max_height:
                max_height = height[i]
                max_index = i
                if max_height >= left_border_val:
                    return max_index
        if i < height_len:
            return max_index
        else:
            return None

    def calSectionWater(self, height: List[int], start: int, stop: int):
        shortter = min(height[start], height[stop])
        sum = 0
        for i in range(start + 1, stop):
            if shortter > height[i]:
                sum += shortter - height[i]
        return sum

    def trap(self, height: List[int]) -> int:
        sum = 0
        index = 0
        while index < len(height):
            left = self.findBorder(height, index)
            right = self.findRightBorder(height, left + 2, height[left])
            if not right:
                break
            sum += self.calSectionWater(height, left, right)
            index = right
        return sum

s = Solution()
print(s.trap(
# [4,2,3]
# [0,1,0,2,1,0,1,3,2,1,2,1]
    [4,7,7,1,0]
))
