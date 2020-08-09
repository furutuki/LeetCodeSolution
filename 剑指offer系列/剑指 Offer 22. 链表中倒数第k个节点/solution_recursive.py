# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def __init__(self):
        self.ans = None

    def search(self, node: ListNode, k: int) -> int:
        if not node:
            return 0
        val = 1 + self.search(node.next, k)
        if val == k:
            self.ans = node
        return val

    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        self.search(head, k)
        return self.ans


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

