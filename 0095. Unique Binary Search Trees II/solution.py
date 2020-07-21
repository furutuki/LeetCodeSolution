# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def doGenerateTrees(self, start: int, end: int) -> List[TreeNode]:
        trees = []
        if start > end:
            trees.append(None)
            return trees

        for i in range(start, end + 1):
            leftTrees = self.doGenerateTrees(start, i - 1)
            rightTrees = self.doGenerateTrees(i + 1, end)
            for leftTree in leftTrees:
                for rightTree in rightTrees:
                    rootNode = TreeNode(i)
                    rootNode.left = leftTree
                    rootNode.right = rightTree
                    trees.append(rootNode)
        return trees

    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.doGenerateTrees(1, n)

s = Solution()
print(s.generateTrees(3))
