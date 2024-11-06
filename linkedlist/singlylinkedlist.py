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

    def delete_from_begin(self):
        if self.head is Node:
            print("Empty linked list")
        else:
            self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            print("Empty linked list")
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
    sll.traverse()
