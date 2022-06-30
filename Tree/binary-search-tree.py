class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if value == temp.value:
                return False
            if new_node.value > temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value > temp.value:
                temp = temp.left
                continue
            if value < temp.value:
                temp = temp.right
                continue
            elif value == temp.value:
                return True


bst = BinarySearchTree()
bst.insert(10)
bst.insert(11)
bst.insert(21)
bst.insert(54)
bst.insert(1)
bst.insert(3)
bst.insert(22)
bst.insert(52)

print(bst.contains(111))
