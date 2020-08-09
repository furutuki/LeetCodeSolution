# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev, cur = dummy, head
        while cur:
            if cur.val == val:
                prev.next = cur.next
                return head if cur != head else prev.next
            prev = cur
            cur = cur.next
        return head