# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        tail = None
        node1 = l1
        node2 = l2
        while node1 and node2:
            if node1.val <= node2.val:
                temp_node = ListNode(node1.val)
                node1 = node1.next
            else:
                temp_node = ListNode(node2.val)
                node2 = node2.next

            if head is None:
                head = temp_node
                tail = temp_node
            else:
                tail.next = temp_node
                tail = temp_node

        while node1:
            temp_node = ListNode(node1.val)
            node1 = node1.next
            if head is None:
                head = temp_node
                tail = temp_node
            else:
                tail.next = temp_node
                tail = temp_node

        while node2:
            temp_node = ListNode(node2.val)
            node2 = node2.next
            if head is None:
                head = temp_node
                tail = temp_node
            else:
                tail.next = temp_node
                tail = temp_node

        return head


