# Definition for a binary tree node.
from typing import List
import collections


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        ret = []
        q = collections.deque()
        q.appendleft(root)

        while q:

            node_list = []
            level_list = []

            while q:
                node = q.pop()
                node_list.append(node)
                level_list.append(node.val)

            ret.append(level_list)

            for item in node_list:
                if item.left:
                    q.appendleft(item.left)
                if item.right:
                    q.appendleft(item.right)
        return ret