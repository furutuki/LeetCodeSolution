from collections import deque
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()
        while head:
            q.appendleft(head)
            head = head.next
        n = 0
        tail = None
        while len(q):
            node = q.pop() if n % 2 == 0 else q.popleft()
            n += 1
            if tail:
                tail.next = node
            tail = node
            tail.next = None
