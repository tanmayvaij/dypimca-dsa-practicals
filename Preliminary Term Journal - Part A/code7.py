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
        self.no_of_nodes = 0

    def insert_at_pos(self, pos, data):
        new_node = Node(data)

        if self.head == None: 
            self.head = self.tail = new_node

        elif pos > self.no_of_nodes + 1:
            print("Out of range")

        elif pos == 1:
            new_node.next = self.head
            self.head = new_node

        elif pos == self.no_of_nodes + 1:
            self.tail.next = new_node
            self.tail = new_node

        else:
            i = 1
            node = self.head
            while i < pos - 1:
                node = node.next
                i+=1
            new_node.next = node.next
            node.next = new_node
            
        self.no_of_nodes += 1

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
sll.insert_at_pos(1, 30)
sll.insert_at_pos(1, 20)
sll.insert_at_pos(2, 6)

sll.traverse()
