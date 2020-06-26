# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        mid = self.getMidofList(head)
        l = head
        r = mid.next
        mid.next = None
        return self.merge(self.sortList(l), self.sortList(r))

    def getMidofList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


    def merge(self, p: ListNode, q: ListNode) -> ListNode:
        tmpNode = ListNode(0)
        h = tmpNode

        while p and q:
            if p.val < q.val:
                h.next = p
                p = p.next
            else:
                h.next = q
                q = q.next

            h = h.next

            if p:
                h.next = p
            if q:
                h.next = q

        return tmpNode.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(3)
e = ListNode(2)
f = ListNode(1)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = None
s = Solution()
h = s.removeDuplicateNodes(a)
while h:
    print(h.val)
    h = h.next


