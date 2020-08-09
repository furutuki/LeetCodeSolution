# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def dfs(self, node: ListNode) -> ListNode:
        if not node:
            return node

        tailnode = node
        nextnode = node.next
        l = self.dfs(nextnode)
        if l:
            cur = l
            while cur.next:
                cur = cur.next
            cur.next = tailnode
            tailnode.next = None
            return l
        else:
            tailnode.next = None
            return tailnode

    def reverseList(self, head: ListNode) -> ListNode:
        return self.dfs(head)


n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
n2.next = None

s = Solution()
l = s.reverseList(n1)
node = l
while node:
    print(node.val)
    node = node.next
