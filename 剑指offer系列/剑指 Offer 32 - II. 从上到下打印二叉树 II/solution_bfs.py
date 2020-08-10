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
            q.appendleft(root)
            while q:
                count = len(q)
                cnt = 0
                level_res = []
                while q and cnt < count:
                    node = q.pop()
                    level_res.append(node.val)
                    if node.left:
                        q.appendleft(node.left)
                    if node.right:
                        q.appendleft(node.right)
                    cnt += 1
                ans.append(level_res)
        return ans