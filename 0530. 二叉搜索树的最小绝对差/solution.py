# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.last_num = -1
        self.min_diff = -1

    def solve(self, node: TreeNode):
        if not node:
            return

        if node.left:
            self.solve(node.left)

        if self.last_num == -1:
            self.last_num = node.val
        else:
            self.min_diff = min(self.min_diff, node.val - self.last_num) if self.min_diff != -1 else node.val - self.last_num
            self.last_num = node.val

        if node.right:
            self.solve(node.right)

    def getMinimumDifference(self, root: TreeNode) -> int:
        self.solve(root)
        return self.min_diff
