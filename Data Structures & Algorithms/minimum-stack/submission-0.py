class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append((value, value))
        else:
            min_val = min(value, self.stack[-1][1])
            self.stack.append((value, min_val))

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]