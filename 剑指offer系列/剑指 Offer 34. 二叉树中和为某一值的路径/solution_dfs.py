# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __self__(self):
        self.ans = []

    def dfs(self, remain: int, node: TreeNode, res: List[int]):
        if not node:
            return

        if not node.left and not node.right:
            if remain == 0:
                self.ans.append(res.copy())
            return

        if node.left:
            res.append(node.left.val)
            self.dfs(remain - node.left.val, node.left, res)
            del res[len(res) - 1]

        if node.right:
            res.append(node.right.val)
            self.dfs(remain - node.right.val, node.right, res)
            del res[len(res) - 1]

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.ans = []
        if root:
            res = [root.val]
            self.dfs(sum - root.val, root, res)
        return self.ans


n1 = TreeNode(-2)
n2 = TreeNode(-3)
n1.right = n2
s = Solution()
print(s.pathSum(n1, -5))
