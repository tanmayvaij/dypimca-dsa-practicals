class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack UnderFlow Error")
        else:
            popped_data = self.top
            self.top = self.top.next
            return popped_data.data

    def peek(self):
        return self.top.data


if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(4)
    s.push(3)
    print(s.pop())
    print(s.peek())
