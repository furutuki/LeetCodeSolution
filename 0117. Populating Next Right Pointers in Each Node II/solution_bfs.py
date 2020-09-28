# Definition for a Node.
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque()
        if not root:
            return None
        q.append(root)
        while True:
            size = len(q)
            cnt = 0
            node, next = None, None
            while cnt < size:
                if cnt == 0:
                    node = q.pop()
                    if node.left:
                        q.appendleft(node.left)
                    if node.right:
                        q.appendleft(node.right)
                    cnt += 1
                if cnt < size:
                    next = q.pop()
                    if next and next.left:
                        q.appendleft(next.left)
                    if next and next.right:
                        q.appendleft(next.right)
                    cnt += 1
                    node.next = next
                    node = next
                else:
                    node.next = None
                    break
            if not len(q):
                break
        return root


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.left = n2
n1.right = n3
s = Solution()
n = s.connect(n1)
print(n)













