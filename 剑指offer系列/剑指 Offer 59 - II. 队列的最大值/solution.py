class MaxQueue:

    def __init__(self):
        self.data = []
        self.ordered_stack = []


    def max_value(self) -> int:
        return -1 if not self.ordered_stack else self.ordered_stack[0]


    def push_back(self, value: int) -> None:
        self.data.append(value)
        while self.ordered_stack and self.ordered_stack[-1] < value:
            self.ordered_stack.pop()
        self.ordered_stack.append(value)

    def pop_front(self) -> int:
        if self.data:
            val = self.data[0]
            del self.data[0]
            if self.ordered_stack and val == self.ordered_stack[0]:
                del self.ordered_stack[0]
            return val
        else:
            return -1




# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()