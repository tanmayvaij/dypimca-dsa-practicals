class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_begin(self, data):
        new_node = Node(data) 
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # def insert_at_end(self, data):
    #     new_node = Node(data)
    #     self.tail

    def traverse(self):
        curr = self.head
        while curr is not None:
            print(f"{curr.data} ->", end=" ")
            curr = curr.next
        print("None")

sll = SinglyLinkedList()
sll.insert_at_begin(10)
sll.traverse()
