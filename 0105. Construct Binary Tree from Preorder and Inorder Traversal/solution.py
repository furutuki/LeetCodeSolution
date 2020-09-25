# Definition for a binary tree node.
# from typing import List


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def solve(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(inorder) == 1:
            return root
        root_idx_inorder = inorder.index(preorder[0])
        lchild = self.solve(preorder[1:root_idx_inorder + 1], inorder[:root_idx_inorder])
        rchild = self.solve(preorder[root_idx_inorder + 1:], inorder[root_idx_inorder + 1:])
        root.left = lchild
        root.right = rchild
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.solve(preorder, inorder)
