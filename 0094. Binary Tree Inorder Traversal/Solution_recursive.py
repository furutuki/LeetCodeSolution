# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def inorder_traversal(self, ret: List[int], root: TreeNode):
        if root is None:
            return

        if root.left is not None:
            self.inorder_traversal(ret, root.left)

        ret.append(root.val)

        if root.right is not None:
            self.inorder_traversal(ret,root.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        self.inorder_traversal(ret, root)
        return ret


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.right = n2
n2.left = n3
s = Solution()
print(s.inorderTraversal(n1))
