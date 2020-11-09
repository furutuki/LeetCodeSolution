# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.data = list()

    def mid_traverse(self, node: TreeNode):
        if not node:
            return
        self.mid_traverse(node.left)
        self.data.append(node.val)
        self.mid_traverse(node.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.mid_traverse(root)
        return self.data[k - 1]