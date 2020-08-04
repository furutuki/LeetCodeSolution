# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head

        prev, cur = dummyNode, head

        """遍历到起点"""
        cnt = 1
        while cur and cnt < m:
            prev = cur
            cur = cur.next
            cnt += 1

        cnt = 0
        while cnt < n - m:
            nextnode = cur.next
            nextnextnode = nextnode.next

            prev_next = prev.next
            prev.next = nextnode
            nextnode.next = prev_next

            cur.next = nextnextnode
            cnt += 1

        return dummyNode.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

n3.next = n5

s = Solution()
l = s.reverseBetween(n3, 1, 2)
node = l
while node:
    print(node.val)
    node = node.next
