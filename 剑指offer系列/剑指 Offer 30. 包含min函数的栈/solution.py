class MinStack:

    def __init__(self):
        self.data = []
        self.mindata = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.mindata:
            self.mindata.append(x)
        elif self.mindata[len(self.mindata) - 1] >= x:
            self.mindata.append(x)

    def pop(self) -> None:
        val = self.data.pop()
        if self.mindata and self.mindata[len(self.mindata) - 1] == val:
            self.mindata.pop()
        return val

    def top(self) -> int:
        return self.data[len(self.data) - 1] if self.data else None

    def min(self) -> int:
        return self.mindata[len(self.mindata) - 1] if self.mindata else None
