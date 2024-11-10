class Stack:

    def __init__(self, size):
        self.top = -1
        self.stack = [ None for _ in range(size)  ]
        self.size = size

    def push(self, data):
        if self.top < self.size - 1:
            self.top += 1
            self.stack[self.top] = data
        else:
            print("Stack Overflow Error")

    def pop(self):
        if self.top > -1:
            popped_data = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return popped_data
        else:
            print("Stack Underflow Error")

    def peek(self):
        return self.stack[self.top]


if __name__ == "__main__":
    s = Stack(5)
    s.push(5)
    s.push(4)
    s.push(3)
    print(s.pop())
    print(s.peek())
