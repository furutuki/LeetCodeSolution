# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        walker = head
        runner = head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                walker2 = head
                while walker != walker2:
                    walker = walker.next
                    walker2 = walker2.next
                return walker
        return None

#
# n1 = ListNode(3)
# n2 = ListNode(2)
# n3 = ListNode(0)
# n4 = ListNode(-4)
#
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next= n2
#
# s = Solution()
# print(s.detectCycle(n1).val)
