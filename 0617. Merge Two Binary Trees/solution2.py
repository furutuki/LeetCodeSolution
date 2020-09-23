# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def solve(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        node = t1
        if t1:
            node.val += t2.val if t2 else 0
        else:
            node = t2
        l = self.solve(t1.left if t1 else None, t2.left if t2 else None)
        r = self.solve(t1.right if t1 else None, t2.right if t2 else None)
        node.left = l
        node.right = r
        return node

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        return self.solve(t1, t2)
