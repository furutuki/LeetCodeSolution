# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, node:TreeNode) -> int:
        if not node:
            return 0

        left = self.dfs(node.left)
        if left == -1:
            return -1

        right = self.dfs(node.right)
        if right == -1:
            return -1

        return -1 if abs(left - right) > 1 else max(left, right) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        return self.dfs(root) != -1