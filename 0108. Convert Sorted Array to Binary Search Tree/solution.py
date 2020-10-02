# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def solve(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        l = self.solve(nums[:mid])
        r = self.solve(nums[mid+1:])
        root.left = l
        root.right = r
        return root


    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.solve(nums)