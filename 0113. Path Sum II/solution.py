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

    def solve(self, node: TreeNode, total: int, target: int, cur_ans: List[int]):
        if not node:
            return
        if not node.left and not node.right:
            if total == target:
                self.ans.append(cur_ans)
            return
        if node.left:
            # cur_ans.append(node.left.val)
            l = cur_ans.copy()
            l.append(node.left.val)
            self.solve(node.left, total + node.left.val, target, l)
            # del cur_ans[len(cur_ans) - 1]
        if node.right:
            # cur_ans.append(node.right.val)
            r = cur_ans.copy()
            r.append(node.right.val)
            self.solve(node.right, total + node.right.val, target, r)
            # del cur_ans[len(cur_ans) - 1]

    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            return []
        self.solve(root, root.val, target, [root.val])
        return self.ans

s = Solution()
root = TreeNode(-2)
leaf = TreeNode(-3)
root.right = leaf

print(s.pathSum(root, -5))