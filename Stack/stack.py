class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def push(self, value):
        new_node = Node(value)
        temp = self.top
        self.top = new_node
        self.top.next = temp
        self.length += 1
        return True

    def pop(self):
        try:
            self.top = self.top.next
            self.length -= 1
            return True
        except AttributeError:
            raise ValueError('Stack is empty')

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next


stack = Stack(10)
stack.push(11)
stack.push(12)
stack.pop()
stack.pop()
stack.print_stack()
