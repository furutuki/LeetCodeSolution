# Definition for a binary tree node.
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = deque()
        ans = []
        if root:
            level = 1
            q.appendleft(root)
            while q:
                count = len(q)
                cnt = 0
                level_res = []
                s = []
                while q and cnt < count:
                    node = q.pop()
                    if level % 2 == 0:
                        s.append(node.val)
                    else:
                        level_res.append(node.val)
                    if node.left:
                        q.appendleft(node.left)
                    if node.right:
                        q.appendleft(node.right)
                    cnt += 1
                while s:
                    level_res.append(s.pop())

                level += 1
                ans.append(level_res)
        return ans
