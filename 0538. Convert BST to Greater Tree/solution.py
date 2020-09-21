# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:


    def __init__(self):
        self.total = 0

    def convertBST(self, root: TreeNode) -> TreeNode:

        def solve(node: TreeNode):
            if not node:
                return
            solve(node.right)
            self.total += node.val
            node.val = self.total
            solve(node.left)

        solve(root)
        return root




s = Solution()
n2 = TreeNode(2)
n1 = TreeNode(1)
n2.left = n1
print(s.convertBST(n2))
