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

    def pop(self):
        if self.head.next is None:
            raise IndexError('DLL is empty')
        temp = self.tail
        prev = self.tail.prev
        del self.tail
        prev.next = None
        self.tail = prev
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        temp = self.head
        self.head.prev = new_node
        new_node.next = temp
        self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            raise IndexError('DLL is empty')
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
        return temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


dll = DublyLinkedList(10)
dll.append(12)
dll.append(14)
dll.pop_first()
dll.print_list()
