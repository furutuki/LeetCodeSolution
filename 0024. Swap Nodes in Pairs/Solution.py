# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = None
        left_node = None
        cur = head
        if cur is not None:
            next_node = cur.next
        while cur is not None and next_node is not None:
            if left_node is not None:
                left_node.next = next_node
            else:
                newHead = next_node

            cur.next = next_node.next
            next_node.next = cur

            left_node = cur
            cur = cur.next
            if cur is not None:
                next_node = cur.next
        if newHead is None and cur is not None:
            newHead = cur
        return newHead


def main():
    s = Solution()
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    one.next = two
    two.next = three
    three.next = four

    new_head = s.swapPairs(one)

    cur_node = new_head
    while cur_node is not None:
        print(cur_node.val)
        cur_node = cur_node.next


if __name__ == '__main__':
    main()
