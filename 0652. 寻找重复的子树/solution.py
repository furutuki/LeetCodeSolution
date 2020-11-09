# Definition for a binary tree node.
from typing import List
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.cnt = defaultdict(int)
        self.ans = []

    def solve(self, node: TreeNode) -> str:
        if not node:
            return "#"
        left = self.solve(node.left)
        right = self.solve(node.right)
        sub_tree = left + "." + right + "." + str(node.val)
        if self.cnt[sub_tree] == 1:
            self.ans.append(node)
        self.cnt[sub_tree] += 1
        return sub_tree

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.solve(root)
        return self.ans


n1 = TreeNode(1)
n2 = TreeNode(2)
n4 = TreeNode(4)
n1.left = n2
n2.left = n4

n3 = TreeNode(3)
n2_2 = TreeNode(2)
n4_2 = TreeNode(4)
n1.right = n3
n3.left = n2_2
n2_2.left = n4_2

s = Solution()
ans = s.findDuplicateSubtrees(n1)
print(ans)
