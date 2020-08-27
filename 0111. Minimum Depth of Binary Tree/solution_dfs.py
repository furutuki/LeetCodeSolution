# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.min_height = -1

    def minDepth(self, root: TreeNode) -> int:

        def dfs(root: TreeNode, step: int):
            if not root:
                return

            step += 1

            if not root.left and not root.right:
                self.min_height = step if self.min_height == 0 else min(self.min_height, step)
                return

            dfs(root.left, step)
            dfs(root.right, step)

        self.min_height = 0
        dfs(root, 0)
        return self.min_height
