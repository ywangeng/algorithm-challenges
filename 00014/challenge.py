"""
Question:

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.

"""


class MaxStack:
    def __init__(self):
        self.stack = []  # main stack
        self.max_stack = []  # auxiliary stack to track max values

    def push(self, val):
        self.stack.append(val)
        # if max_stack is empty OR val >= current max, push it to max_stack
        if not self.max_stack or val >= self.max_stack[-1]:
            self.max_stack.append(val)

    def pop(self):
        if not self.stack:
            return None  # or raise IndexError("pop from empty stack")
        val = self.stack.pop()
        if val == self.max_stack[-1]:
            self.max_stack.pop()
        return val

    def max(self):
        if not self.max_stack:
            return None  # or raise ValueError("max from empty stack")
        return self.max_stack[-1]
