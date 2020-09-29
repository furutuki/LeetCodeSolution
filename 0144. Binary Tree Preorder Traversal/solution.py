# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ans = []
        node = root
        while node or len(stack):
            while node:
                ans.append(node.val)
                stack.append(node)
                node = node.left
            if len(stack):
                cur = stack.pop()
                node = cur.right
        return ans
