class MinStack:
    def __init__(self):
        # main_stack stores all elements
        self.main_stack = []
        # min_stack stores the minimum value at each state
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        # If min_stack is empty or val is new minimum, push it
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            # Otherwise, repeat the current minimum
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.main_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
