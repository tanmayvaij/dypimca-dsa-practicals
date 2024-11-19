class Node:
    
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert_node(self, data):
        new_node = Node(data)

        if self.root is None: self.root = new_node
        else:
            curr = self.root
            while curr is not None:
                
                if data > curr.data:
                    if curr.right is None:
                        curr.right = new_node
                        break
                    else:
                        curr = curr.right

                if data < curr.data:
                    if curr.left is None:
                        curr.left = new_node
                        break
                    else:
                        curr = curr.left

    def display(self):
        stack = [ self.root ]
        while stack:
            node = stack.pop()
            print(node.data, end=" ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def printInOrder(self):
        stack = []
        curr = self.root

        while curr is not None or stack:

            while curr is not None:
                stack.append(curr)
                curr = curr.left

            node = stack.pop()
            print(node.data, end=" ")

            curr = node.right

    def printPostOrder(self):
        stack = []
        curr = self.root

        while curr is not None or stack:

            while curr is not None:
                stack.append(curr)
                curr = curr.left

            node = stack.pop()
            print(node.data, end=" ")

            curr = node.right

            
bst = BinarySearchTree()

bst.insert_node(9)
bst.insert_node(5)
bst.insert_node(4)
bst.insert_node(6)
bst.insert_node(8)
bst.insert_node(10)
bst.insert_node(1)

bst.display()
