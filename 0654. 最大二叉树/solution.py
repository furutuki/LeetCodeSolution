# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMax(self, nums: List[int]) -> List[int]:
        idx, max_val = 0, nums[0]
        for i in range(1, len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
                idx = i
        return [idx, max_val]

    def solve(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        ret = self.findMax(nums)
        root = TreeNode(ret[1])
        l = self.solve(nums[:ret[0]])
        r = self.solve(nums[ret[0] + 1:])
        root.left = l
        root.right = r
        return root

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.solve(nums)

