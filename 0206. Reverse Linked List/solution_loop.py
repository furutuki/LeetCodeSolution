# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummyNode = ListNode(0)
        prev, cur = dummyNode, head
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        head.next = None
        return prev


n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
n2.next = None

s = Solution()
l = s.reverseList(n2)
node = l
while node:
    print(node.val)
    node = node.next
