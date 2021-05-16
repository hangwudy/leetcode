class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_min = list()
        self.stack = list()

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.stack_min:
            self.stack_min.append(x)
        elif self.stack_min[-1] > x:
            self.stack_min.append(x)
        elif self.stack_min[-1] <= x:
            self.stack_min.append(self.stack_min[-1])

    def pop(self) -> None:
        self.stack_min.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.stack_min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
