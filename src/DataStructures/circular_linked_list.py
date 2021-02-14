class Node:
    next = None

    def __init__(self, data):
        self.data = data

class CircularLinkedList:
    size = 0
    head = None

    def add(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            node.next = self.head
            self.size += 1
        elif self.head == self.head.next:
            node.next = self.head
            self.head.next = node
            self.head = node
            self.size += 1
        else:
            current = self.head

            while current.next is not self.head:
                current = current.next

            node.next = self.head
            self.head = node
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

    def add_after(self, data, node_data):
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

    def add_at_index(self, data, index):
        node = Node(data)

        if self.head is None and index != 0:
            return False

        if index == 0:
            if self.head is None:
                self.head = node
                self.head.next = self.head
            else:
                current = self.head

                while current.next is not self.head:
                    current = current.next
            
                node.next = self.head
                self.head = node
                current.next = self.head
        else:
            if self.head is None:
                return False

            prev = None
            current = self.head
            count = 0

            while current.next is not self.head and count != index:
                prev = current
                current = current.next
                count += 1
            
            if count != index:
                return False

            node.next = current
            prev.next = node

    def remove(self, data):
        if self.head is None:
            return False
            
        prev = None
        current = self.head

        while current.data != data and current.next is not self.head:
            prev = current
            current = current.next

        if current.data != data:
            return False
        
        if self.head.next == self.head:
            self.head = None
            self.size -= 1
        elif current == self.head:
            prev = self.head

            while prev.next is not self.head:
                prev = prev.next

            self.head = self.head.next
            prev.next = self.head
            self.size -= 1
        elif current.next == self.head:
            prev.next = self.head
            self.size -= 1
        else:
            prev.next = current.next
            self.size -= 1
                
    def print_nodes(self):
        '''Print all nodes in list'''
        if self.head is None:
            return False

        current = self.head
        nodes = ""

        while current.next != self.head:
            nodes += str(current.data) + ' --> '
            current = current.next

        print(nodes + str(current.data) + ' --> Head')