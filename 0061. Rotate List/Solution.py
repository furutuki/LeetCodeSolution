# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        len = 0
        tail = None
        node = head
        while node:
            len += 1
            tail = node
            node = node.next

        k %= len
        if k == 0:
            return head

        idx = 1
        node = head
        while idx < len - k:
            node = node.next
            idx += 1

        newhead = node.next
        node.next = None
        tail.next = head
        return newhead


s = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)
# n5 = ListNode(5)
n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

res = s.rotateRight(n1, 1)
print(res)