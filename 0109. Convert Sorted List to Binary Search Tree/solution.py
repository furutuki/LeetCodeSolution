# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def solve(self, nodelist:List[int], start: int, end: int):
        if start > end:
            return None
        elif start == end:
            return TreeNode(nodelist[start])

        mid = (end - start + 1) // 2 + start
        node = TreeNode(nodelist[mid])
        leftTree = self.solve(nodelist, start, mid - 1)
        rightTree = self.solve(nodelist, mid + 1, end)
        node.left = leftTree
        node.right = rightTree
        return node

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nodelist = []
        while head:
            nodelist.append(head.val)
            head = head.next

        return self.solve(nodelist, 0, len(nodelist) - 1)


n1 = ListNode(-10)
n2 = ListNode(-3)
n3 = ListNode(0)
n4 = ListNode(5)
n5 = ListNode(9)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
s = Solution()
head = s.sortedListToBST(n1)
print(head)
