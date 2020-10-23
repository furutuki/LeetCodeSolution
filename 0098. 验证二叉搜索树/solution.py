# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.cur_node = None

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if self.cur_node and root.val <= self.cur_node.val:
            return False
        self.cur_node = root
        if not self.isValidBST(root.right):
            return False
        return True

n1 = TreeNode(1)
n2 = TreeNode(1)
n1.left = n2
s = Solution()
print(s.isValidBST(n1))