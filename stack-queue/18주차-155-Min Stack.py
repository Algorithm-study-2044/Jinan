class MinStack:
    def __init__(self):
        # Initialize two stacks: one for the stack elements, and one for the minimum elements
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push to min_stack if it's empty or the new val is <= the current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            # Pop from min_stack if the value to pop is the current minimum
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        # Return the top element of the stack
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        # Return the top element of the min_stack, which is the current minimum
        return self.min_stack[-1] if self.min_stack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
