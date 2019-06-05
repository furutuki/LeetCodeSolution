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
    def isPalindrome(self, head: ListNode) -> bool:
        node = head
        prev_node_ex = None

        if head is None:
            return True

        while node is not None:
            node_ex = ListNodeEx(node)
            node_ex.prev = prev_node_ex
            prev_node_ex = node_ex
            node = node.next

        head_node = head
        tail_node_ex = prev_node_ex

        while head_node is not None and tail_node_ex is not None:
            if head_node == tail_node_ex.node:
                return True
            elif head_node.val == tail_node_ex.node.val:
                if head_node.next == tail_node_ex.node:
                    return True
                elif tail_node_ex.node.next == head_node:
                    return True
                head_node = head_node.next
                tail_node_ex = tail_node_ex.prev
                continue
            else:
                return False


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Solution()
print(s.isPalindrome(node1))


