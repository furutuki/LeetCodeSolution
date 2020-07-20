# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def doBuildTree(self, preorder: List[int], start: int, end: int,
                    inorder: List[int], start2: int, end2: int) -> TreeNode:

        if start > end or start2 > end2:
            return None

        preorder_root_index = start
        node = TreeNode(preorder[preorder_root_index])

        inorder_root_index = inorder.index(preorder[preorder_root_index], start2, end2 + 1)

        leftChild = self.doBuildTree(preorder, start + 1, start + inorder_root_index - start2,
                                     inorder, start2, inorder_root_index - 1)

        rightChild = self.doBuildTree(preorder, start + 1 + inorder_root_index - start2, end,
                                      inorder, inorder_root_index + 1, end2)

        node.left = leftChild
        node.right = rightChild

        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.doBuildTree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


s = Solution()
print(s.buildTree([3],[3]))
# print(s.buildTree([3,9,20,15,7], [9,3,15,20,7]))
