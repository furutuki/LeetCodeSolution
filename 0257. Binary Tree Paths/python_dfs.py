# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = []

    def dfs(self, node: TreeNode, res:str):
        if not node:
            return

        res += str(node.val)

        if not node.left and not node.right:
            if res:
                self.ans.append(res)
        else:
            res += "->"
            self.dfs(node.left, res)
            self.dfs(node.right, res)



    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.dfs(root, "")
        return self.ans

