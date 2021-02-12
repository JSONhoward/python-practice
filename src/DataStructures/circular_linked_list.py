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
        elif self.head == self.head.next:
            self.head.next = node
            node.next = self.head
            self.head = node
            self.size += 1
        else:
            node.next = self.head
            self.head = node

            current = self.head

            while current.next is not self.head:
                current = current.next

            current.next = self.head
            self.size += 1

    def add_at_tail(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.head.next = self.head
            self.size += 1
        elif self.head == self.head.next:
            node.next = self.head
            self.head.next = node
            self.size += 1
        else:
            current = self.head

            while current.next is not self.head:
                current = current.next

            current.next = node
            node.next = self.head
            self.size += 1

    def add_after(self, node_data, data):
        node = Node(data)

        if self.head is None:
            return False
        elif self.head == self.head.next and self.head.data == node_data:
            node.next = self.head
            self.head.next = node
            self.size += 1
        else:
            current = self.head

            while current.data != node_data and current.next is not self.head:
                current = current.next

            if current.data != node_data:
                return False
            
            node.next = current.next
            current.next = node
            self.size += 1