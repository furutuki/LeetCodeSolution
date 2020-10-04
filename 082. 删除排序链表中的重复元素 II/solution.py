# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(-9999999999)
        dummy_head.next = head
        prev = dummy_head
        while prev and prev.next:
            cur = prev.next
            if not cur.next or cur.next.val != cur.val:
                prev = cur
            else:
                while cur.next and cur.next.val == cur.val:
                    cur = cur.next
                prev.next = cur.next

        return dummy_head.next
