"""
Create Singly linked list and perform the following operations:
a) Insert from start b) Insert from end c) Traverse
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = self.tail = None

    def insert_at_begin(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    def traverse(self):
        if self.head == None:
            print("Empty Linked List")

        else:
            node = self.head
            while node != None:
                print(f"{node.data} ->", end=" ")
                node = node.next
            print("None")

sll = SinglyLinkedList()
sll.insert_at_begin(30)
sll.insert_at_begin(20)
sll.insert_at_begin(10)

sll.insert_at_end(40)
sll.insert_at_end(50)

sll.traverse()
