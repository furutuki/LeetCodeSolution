from typing import List

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, postorder: List[int], midorder: List[int]) -> TreeNode:
        if not postorder:
            return None

        node = TreeNode(postorder[-1])
        root_index_midorder = midorder.index(postorder[-1])
        midorder_leftsubtree = midorder[:root_index_midorder]
        midorder_rightsubtree = midorder[root_index_midorder + 1:]
        postorder_leftsubtree = []
        postorder_rightsubtree = []

        for i in range(len(postorder) - 1):
            if midorder_leftsubtree.__contains__(postorder[i]):
                postorder_leftsubtree.append(postorder[i])
            else:
                postorder_rightsubtree.append(postorder[i])

        leftsubtree = self.buildTree(postorder_leftsubtree, midorder_leftsubtree)
        rightsubtree = self.buildTree(postorder_rightsubtree, midorder_rightsubtree)
        node.left = leftsubtree
        node.right = rightsubtree
        return node

    def postTraverse(self, root: TreeNode, postorder: List[int]):
        if not root:
            return
        self.postTraverse(root.left, postorder)
        self.postTraverse(root.right, postorder)
        postorder.append(root.val)

    def verifyPostorder(self, postorder: List[int]) -> bool:
        midorder = sorted(postorder)
        tree = self.buildTree(postorder, midorder)
        postorder2 = []
        self.postTraverse(tree, postorder2)

        return postorder == postorder2


s = Solution()
t = s.verifyPostorder([1,6,3,2,5])
t2 = s.verifyPostorder([1,3,2,6,5])
print(t)
print(t2)

