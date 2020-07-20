class Stack:

    def __init__(self):
        self.data = []

    def push(self, val: int):
        self.data.append(val)

    def pop(self) -> int:
        return self.data.pop()

    def empty(self) -> bool:
        return len(self.data) == 0


class CQueue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def appendTail(self, value: int) -> None:
        self.s1.push(value)

    def deleteHead(self) -> int:
        val = -1
        while not self.s1.empty():
            self.s2.push(self.s1.pop())
        if not self.s2.empty():
            val = self.s2.pop()
        while not self.s2.empty():
            self.s1.push(self.s2.pop())
        return val

# Your CQueue object will be instantiated and called as such:
obj = CQueue()
obj.appendTail(3)
print(obj.deleteHead())
print(obj.deleteHead())
