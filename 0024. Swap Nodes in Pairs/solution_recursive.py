# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def solve(self, prev: ListNode):
        if not prev or not prev.next or not prev.next.next:
            return
        cur = prev.next
        next = cur.next
        tmp = next.next
        cur.next = tmp
        next.next = cur
        prev.next = next
        prev = cur
        self.solve(prev)


    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_ndoe = ListNode(0)
        dummy_ndoe.next = head
        self.solve(dummy_ndoe)
        return dummy_ndoe.next
