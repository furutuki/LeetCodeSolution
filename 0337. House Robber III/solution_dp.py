# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def dfs(self, node: TreeNode, cache: dict) -> int:
        if not node:
            return 0

        if cache.__contains__(node):
            return cache[node]

        val1 = node.val
        if node.left:
            val1 += self.dfs(node.left.left, cache) + self.dfs(node.left.right, cache)
        if node.right:
            val1 += self.dfs(node.right.left, cache) + self.dfs(node.right.right, cache)

        val2 = self.dfs(node.left, cache) + self.dfs(node.right, cache)
        ans = max(val1, val2)
        cache[node] = ans
        return ans

    def rob(self, root: TreeNode) -> int:
        cache = dict()
        return self.dfs(root, cache)
