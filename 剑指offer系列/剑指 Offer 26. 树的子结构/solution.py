# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """B中的节点是否都在A为根的树中并且结构一样"""
    def judge(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return True
        if not A:
            return False
        if A.val != B.val:
            return False
        return self.judge(A.left, B.left) and self.judge(A.right, B.right)

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        return self.judge(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)