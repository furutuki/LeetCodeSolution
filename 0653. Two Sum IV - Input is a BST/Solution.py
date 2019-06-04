class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def midAccessTree(self, node: TreeNode):
        res = []

        if node.left is not None:
            res.extend(self.midAccessTree(node.left))

        res.append(node.val)

        if node.right is not None:
            res.extend(self.midAccessTree(node.right))

        return res

    def twoSum(self, nums: 'List[int]', target: int):
        start = 0
        end = len(nums) - 1
        while start < end :
            if nums[start] + nums[end] > target:
                end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                return True
        return False

    def findTarget(self, root: TreeNode, k: int) -> bool:
        res = self.midAccessTree(root)
        return self.twoSum(res, k)


s = Solution()
root = TreeNode(5)
node3 = TreeNode(3)
node6 = TreeNode(6)
node2 = TreeNode(2)
node4 = TreeNode(4)
node7 = TreeNode(7)
root.left = node3
root.right = node6
node3.left = node2
node3.right = node4
node6.right = node7

print(s.findTarget(root, 9))
print(s.findTarget(root, 28))
