# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNodeEx:
    def __init__(self, node):
        self.node = node
        self.prev = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev = None
        cur_node = head
        while cur_node is not None:
            new_node = ListNodeEx(cur_node)
            new_node.prev = prev
            prev = new_node
            cur_node = cur_node.next

        tail = prev
        cur_node_ex = tail

        if n == 1:
            if tail.prev is None:
                return None
            else:
                tail.prev.node.next = None
                return head

        x = 0

        while x < n - 2 and cur_node_ex is not None:
            x += 1
            cur_node_ex = cur_node_ex.prev
        to_be_removed_node_ex = cur_node_ex.prev

        if to_be_removed_node_ex.prev is not None:
            to_be_removed_node_ex.prev.node.next = cur_node_ex.node
            return head
        else:
            return cur_node_ex.node


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = None
# node3.next = node4
# node4.next = node5

s = Solution()
head = s.removeNthFromEnd(node1, 2)
while head is not None:
    print(head.val)
    head = head.next
