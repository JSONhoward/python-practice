class Node:
    next = None

    def __init__(self, data):
        self.data = data

class CircularLinkedList:
    size = 0

    def __init__(self, head):
        self.head = None

    def add(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.head.next = self.head
            self.size += 1
        else:
            current = self.head

            while current.next is not self.head:
                current = current.next

            current.next = node
            node.next = self.head
            self.size += 1