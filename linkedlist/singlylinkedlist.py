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
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data) 
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_pos(self, data, pos):
        new_node = Node(data) 
        if self.head is None:
            self.head = self.tail = new_node   
        elif pos == 1:
            self.insert_at_begin(data)
        else:
            i = 1
            curr = self.head
            while i < pos - 1:
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node

    def delete_from_begin(self):
        if self.head is Node:
            print("Empty linked list")
        else:
            self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            print("Empty linked list")
        elif self.head.next is None:
            self.head = self.tail = None
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None
            self.tail = curr

    def traverse(self):
        curr = self.head
        while curr is not None:
            print(f"{curr.data} ->", end=" ")
            curr = curr.next
        print("None")

if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_begin(10)
    sll.insert_at_begin(20)
    sll.insert_at_begin(30)
    sll.insert_at_pos(40, 2)
    sll.traverse()
