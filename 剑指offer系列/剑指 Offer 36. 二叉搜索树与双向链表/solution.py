# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def midTraverse(self, node: Node, ans: List[Node]):
        if node:
            self.midTraverse(node.left, ans)
            ans.append(node)
            self.midTraverse(node.right, ans)

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root:
            ans = []
            self.midTraverse(root, ans)
            n = len(ans)
            for i in range(n):
                ans[i].right = ans[(i + 1) % n]
                ans[(i + 1) % n].left = ans[i]
            return ans[0]
        else:
            return None