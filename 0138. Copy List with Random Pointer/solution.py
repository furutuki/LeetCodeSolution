"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def doCopyRandomList(self, head: 'Node', mapping: dict):
        if not head:
            return None
        elif head in mapping:
            return mapping.get(head)

        newHead = Node(head.val, None, None)
        mapping[head] = newHead
        newHead.next = self.doCopyRandomList(head.next, mapping)
        newHead.random = self.doCopyRandomList(head.random, mapping)
        return newHead

    def copyRandomList(self, head: 'Node') -> 'Node':
        return self.doCopyRandomList(head, {})