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
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, value, index):
        if not isinstance(value or index, int):
            raise TypeError('must be int')
        temp = self.get(index)
        temp.value = value
        return temp
    
    def insert(self, value, index):
        if index == self.length:
            new_node = self.append(value)
            return new_node
        temp = self.get(index - 1)
        temp_next = temp.next
        new_node = Node(value)
        temp.next = new_node
        new_node.next = temp_next
        self.length += 1
        return new_node

    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError('Index out of range')
        temp_back = self.get(index - 1)
        temp_next = self.get(index + 1)
        temp_back.next = temp_next
        self.length -= 1
        return True
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


linked_list = LinkedList(1)
linked_list.append(9)
linked_list.append(8)
linked_list.append(3)
linked_list.print_list()
