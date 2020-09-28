# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def preorder(self, root: TreeNode, res: List[TreeNode]):
        if not root:
            return
        res.append(root)
        if root.left:
            self.preorder(root.left, res)
        if root.right:
            self.preorder(root.right, res)

    def flatten(self, root: TreeNode) -> None:
        ans = []
        self.preorder(root, ans)
        for i in range(len(ans)):
            ans[i].left = None
            if i + 1 < len(ans):
                ans[i].right = ans[i + 1]
