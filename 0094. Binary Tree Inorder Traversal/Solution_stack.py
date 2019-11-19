# Definition for a binary tree node.
from queue import LifoQueue
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        stack = LifoQueue()
        p = root

        while not stack.empty() or p:
            while p:
                stack.put(p)
                p = p.left

            if not stack.empty():
                node = stack.get()
                ret.append(node.val)
                p = node.right

        return ret



n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.right = n2
n2.left = n3
s = Solution()
print(s.inorderTraversal(n1))