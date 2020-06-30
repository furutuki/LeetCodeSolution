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
        if not self.s2.empty():
            return self.s2.pop()
        elif self.s1.empty():
            return -1
        else:
            while not self.s1.empty():
                self.s2.push(self.s1.pop())
            return self.s2.pop()

# Your CQueue object will be instantiated and called as such:
obj = CQueue()
obj.appendTail(5)
obj.appendTail(2)
print(obj.deleteHead())
print(obj.deleteHead())
