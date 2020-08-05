# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = slow = head
        cnt = 0
        while cnt < k and fast:
            fast = fast.next
            cnt += 1
        while fast:
            slow = slow.next
            fast = fast.next
        return slow



s = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
node = s.getKthFromEnd(n1, 2)
cur = node
while cur:
    print(cur.val)
    cur = cur.next

