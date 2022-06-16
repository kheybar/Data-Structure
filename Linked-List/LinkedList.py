class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
   

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            raise IndexError('LinkedList is empty')
        else:
            temp = self.head
            pre = self.head
            while (temp.next):
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            raise IndexError('LinkedList is empty')
        else:
            self.head = self.head.next
            self.head.next = self.head.next
            self.length -= 1
            return True

    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError('Index out of range')
        item = self.head
        for _ in range(index):
            item = item.next
        return item.value

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


linked_list = LinkedList(1)
linked_list.append(9)
linked_list.print_list()
