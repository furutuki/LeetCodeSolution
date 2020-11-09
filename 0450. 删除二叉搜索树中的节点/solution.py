# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            node = self.getMinVal(root.right)
            root.val = node.val
            root.right = self.deleteNode(root.right, node.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def getMinVal(self, root: TreeNode) -> TreeNode:
        while root.left:
            root = root.left
        return root

n5 = TreeNode(5)
n3 = TreeNode(3)
n6 = TreeNode(6)
n2 = TreeNode(2)
n4 = TreeNode(4)
n7 = TreeNode(7)
n5.left = n3
n5.right = n6
# n3.left = n2
# n3.right = n4
# n6.right = n7
s = Solution()
ans = s.deleteNode(n5, 3)
print(ans)
