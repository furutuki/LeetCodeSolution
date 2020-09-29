# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
借鉴终须遍历的思路（根左右），求出根右左的遍历顺序，然后列表反过来就是左右根（后续遍历）的列表
"""


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        node = root
        while node or len(stack):
            while node:
                ans.append(node.val)
                stack.append(node)
                node = node.right
            if len(stack):
                cur = stack.pop()
                node = cur.left
        ans.reverse()
        return ans


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.right = n2
n2.left = n3
s = Solution()
l = s.postorderTraversal(n1)
for item in l:
    print(item)
