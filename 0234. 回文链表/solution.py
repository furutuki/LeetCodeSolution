# Definition for singly-linked list.
from collections import deque

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = deque()
        while head:
            q.appendleft(head)
            head = head.next
        while len(q):
            l = q.popleft()
            if not len(q):
                return True
            r = q.pop()
            if l.val != r.val:
                return False
        return True



