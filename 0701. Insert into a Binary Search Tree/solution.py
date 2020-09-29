# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solve(self, node: TreeNode, val: int):
        if not node:
            return

        if val < node.val:
            if node.left:
                self.solve(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self.solve(node.right, val)
            else:
                node.right = TreeNode(val)

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        self.solve(root, val)
        return root

