class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


dll = DublyLinkedList(10)
dll.append(12)
dll.append(12)
dll.print_list()
