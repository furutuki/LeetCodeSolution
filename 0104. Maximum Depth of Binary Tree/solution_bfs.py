# Definition for a binary tree node.
from typing import List
import collections


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        q = collections.deque()
        q.appendleft(root)
        height = 0

        while q:
            node_list = []
            while q:
                node = q.pop()
                node_list.append(node)
            height += 1

            for item in node_list:
                if item.left:
                    q.appendleft(item.left)
                if item.right:
                    q.appendleft(item.right)
        return height