# Definition for a binary tree node.
# from typing import List


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def solve(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        if len(inorder) == 1:
            return root
        root_idx_inorder = inorder.index(postorder[-1])
        lchild = self.solve(inorder[:root_idx_inorder], postorder[:root_idx_inorder])
        rchild = self.solve(inorder[root_idx_inorder + 1:], postorder[root_idx_inorder : len(postorder) - 1])
        root.left = lchild
        root.right = rchild
        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.solve(inorder, postorder)
