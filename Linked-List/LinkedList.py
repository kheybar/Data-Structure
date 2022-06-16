class Node:
    def __init__(self, value):
        self.value = value
        self.tail = None


class LinkedList:
    def __init__(self, value):
        mew_node = Node(value)
        self.head = mew_node
        self.tail = mew_node
        self.length = 1
