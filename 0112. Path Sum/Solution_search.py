# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right and sum - root.val == 0:
            return True

        if root.left:
            res = self.hasPathSum(root.left, sum - root.val)
            if res:
                return True

        if root.right:
            res = self.hasPathSum(root.right, sum - root.val)
            if res:
                return True

        return False


s = Solution()
root = TreeNode(-2)
leaf = TreeNode(-3)
root.right = leaf

print(s.hasPathSum(root, -5))
