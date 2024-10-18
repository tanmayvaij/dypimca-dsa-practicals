class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.head.prev = new_node

    def insert_at_pos(self, pos, data):
        new_node = Node(data)
        if pos == 1:
            self.insert_at_begin(data)
        else:
            current = self.head
            for _ in range(pos - 1):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            new_node.prev = curr
            curr.next = new_node

    def delete_at_begin(self):
        if self.head is None: 
            print("List is empty")
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_at_pos(self, pos):
        if pos == 1:
            self.delete_at_begin()
        else:
            curr = self.head
            for _ in range(1,pos-1):
                curr = curr.next
            curr.next = curr.next.next
            curr.next.prev = curr

    def delete_at_end(self):
        if self.head is None: 
            print("List is empty")        
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None
            
    def traverse(self):
        curr = self.head
        while curr:
            print(f"{curr.data} ->", end=" ")
            curr = curr.next
        print("None")

if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    dll.insert_at_begin(30)
    dll.insert_at_begin(20)
    dll.insert_at_begin(10)
    
    dll.traverse()
    
    dll.insert_at_end(40)
    dll.insert_at_end(50)
    dll.insert_at_end(60)
    
    dll.traverse()
    
    dll.delete_at_begin()
    dll.delete_at_end()
    
    dll.traverse()
    
    dll.insert_at_pos(2, 35)
    
    dll.traverse()
  
    dll.delete_at_pos(2)
    
    dll.traverse()

