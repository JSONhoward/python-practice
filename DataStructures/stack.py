class Stack:
    size = 0
    stack = []

    def __init__(self, max_size = 100):
        self.max_size = max_size

    def push(self, data):
        if self.size >= self.max_size:
            return False
        self.stack.insert(0, data)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return
        self.stack.pop(0)
        self.size -= 1

    def peek(self):
        return self.stack[0]

    def full(self):
        return self.size == self.max_size

    def print_stack(self):
        for i in self.stack:
            print(i)