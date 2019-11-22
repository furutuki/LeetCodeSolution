# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def recursive_traversal(self, left: TreeNode, right: TreeNode):
        if not left or not right:
            return left == right
        elif left.val != right.val:
            return False
        return self.recursive_traversal(left.left, right.right) and self.recursive_traversal(left.right, right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.recursive_traversal(root.left, root.right)
