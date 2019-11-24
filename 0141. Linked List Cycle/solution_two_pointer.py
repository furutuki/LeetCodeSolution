# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p = head
        q = head
        while p and q:
            if not q:
                break
            elif q.next == p:
                return True

            q = q.next
            if not q:
                break
            elif q.next == p:
                return True
            q = q.next
            p = p.next
        return False


n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(-4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next= n2

s = Solution()
print(s.hasCycle(n1))
