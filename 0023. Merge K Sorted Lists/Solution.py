import heapq


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    # def __lt__(self, other):
    #     return self.val < other.val


class Solution:

    def mergeKLists(self, lists):

        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val

        heap = []
        for node in lists:
            head = node
            while head is not None:
                heapq.heappush(heap, Wrapper(head))
                head = head.next

        if len(heap) == 0:
            return None
        else:
            head = ListNode(0)
            tail = head
            for i in range(len(heap)):
                wrapper_node = heapq.heappop(heap)
                item = wrapper_node.node
                # item = heapq.heappop(heap)
                item.next = None
                tail.next = item
                tail = item
            return head.next

    def listNodeToString(self, node):
        if not node:
            return "[]"

        result = ""
        while node:
            result += str(node.val) + ", "
            node = node.next
        return "[" + result[:-2] + "]"

s = Solution()
n1 = ListNode(1)
n2 = ListNode(4)
n3 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = None

p1 = ListNode(1)
p3 = ListNode(3)
p4 = ListNode(4)
p1.next = p3
p3.next = p4
p4.next = None

d1 = ListNode(2)
d3 = ListNode(6)
d1.next = d3
d3.next = None
listnode = s.mergeKLists([n1, p1, d1])
res = s.listNodeToString(listnode)
print(res)
