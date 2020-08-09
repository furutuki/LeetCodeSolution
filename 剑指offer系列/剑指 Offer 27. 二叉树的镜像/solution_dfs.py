# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, node: TreeNode):
        if not node:
            return
        node.left, node.right = node.right, node.left
        self.dfs(node.left)
        self.dfs(node.right)

    def mirrorTree(self, root: TreeNode) -> TreeNode:
        self.dfs(root)
        return root