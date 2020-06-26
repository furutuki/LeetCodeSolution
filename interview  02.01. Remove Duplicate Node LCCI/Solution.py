# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:


        if not head or not head.next:
            return head

        f = [False for i in range(20001)]

        f[head.val] = True
        prev_node = head
        cur_node = head.next

        while cur_node:
            if f[cur_node.val]:
                cur_node = cur_node.next
                prev_node.next = cur_node
            else:
                f[cur_node.val] = True
                prev_node = cur_node
                cur_node = cur_node.next
        return head


