class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        self.last.next = new_node
        self.last = new_node
        self.length += 1
        return True
    
    def dequeue(self):
        try:
            self.first = self.first.next
            self.length -= 1
        except AttributeError:
            raise ValueError('Queue is empty')
        return True

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next


queue = Queue(10)
queue.enqueue(11)
queue.enqueue(12)
queue.dequeue()
queue.dequeue()
queue.print_queue()
