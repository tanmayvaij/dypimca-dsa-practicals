class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = new_node
        else:
            curr = self.head
            while curr.next is not self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = new_node
        else:
            curr = self.head
            while curr.next is not self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    def insert_at_pos(self, data, pos):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = new_node
        elif pos == 1:
            self.insert_at_begin(data)
        else:
            curr = self.head
            for _ in range(1, pos - 1):
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node

    def delete_from_begin(self):
        if self.head is None:
            print("Empty Linked List")
        elif self.head.next is self.head:
            self.head = None
        else:
            curr = self.head
            while curr.next is not self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = curr.next

    def delete_from_end(self):
        if self.head is None:
            print("Empty Linked List")
        elif self.head.next is self.head:
            self.head = None
        else:
            curr = self.head
            while curr.next.next is not self.head:
                curr = curr.next
            curr.next = self.head

    def delete_from_pos(self, pos):
        if self.head is None:
            print("Empty Linked List")
        elif pos == 1:
            self.delete_from_begin()
        else:
            curr = self.head
            for _ in range(1, pos - 1):
                curr = curr.next
            curr.next = curr.next.next

    def traverse(self):
        curr = self.head
        while curr.next is not self.head:
            print(f"{curr.data} -> ", end=" ")
            curr = curr.next
        print(curr.data)


if __name__ == "__main__":
    scll = SinglyCircularLinkedList()

    scll.insert_at_begin(40)
    scll.insert_at_begin(30)
    scll.insert_at_begin(20)

    scll.insert_at_end(50)
    scll.insert_at_end(60)
    scll.insert_at_end(70)

    scll.insert_at_pos(66, 3)

    scll.delete_from_begin()
    scll.delete_from_begin()

    scll.delete_from_end()

    scll.traverse()
