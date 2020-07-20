# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Stack:
    def __init__(self):
        self.list = list()

    def empty(self):
        return len(self.list) == 0

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if len(self.list) > 0:
            return self.list.pop(self.list.__len__() - 1)

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []

        s = Stack()
        node = head
        while node:
            s.push(node.val)
            node = node.next
        res = []
        while not s.empty():
            res.append(s.pop())
        return res