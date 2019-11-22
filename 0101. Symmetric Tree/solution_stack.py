# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from queue import LifoQueue

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def putNode(node):
            if not node:
                stack.put("null")
            else:
                stack.put(node)
        
        def isNoneNode(node):
            return node == "null"

        if not root:
            return True
        
        stack = LifoQueue()
        putNode(root.left)
        putNode(root.right)
        while not stack.empty():
            node1 = stack.get()
            node2 = stack.get()
            if isNoneNode(node1) and isNoneNode(node2):
                continue
            elif isNoneNode(node1)or isNoneNode(node2) or node1.val != node2.val:
                return False
            putNode(node1.left)
            putNode(node2.right)
            putNode(node1.right)
            putNode(node2.left)
        return True

        #
        # stack = LifoQueue()
        # stack.put(root.left)
        # stack.put(root.right)
        # while not stack.empty():
        #     node1 = stack.get()
        #     node2 = stack.get()
        #     if not node1 and not node2:
        #         continue
        #     elif not node1 or not node2 or node1.val != node2.val:
        #         return False
        #     stack.put(node1.left)
        #     stack.put(node2.right)
        #     stack.put(node1.right)
        #     stack.put(node2.left)
        # return True

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(2)
n1.left = n2
n1.right = n3

s = Solution()
print(s.isSymmetric(None))


