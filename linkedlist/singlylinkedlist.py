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
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        curr = self.head
        while curr is not None:
            print(f"{curr.data} ->", end=" ")
            curr = curr.next
        print("None")

sll = SinglyLinkedList()
sll.insert_at_begin(10)
sll.traverse()
