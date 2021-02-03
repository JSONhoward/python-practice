class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data

class Linked_List:
    head = None
    size = 0

    def add(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.size += 1
            return
        else:
            node.next = self.head
            self.head = node
            self.size += 1

    def add_after(self, node_data, data):
        node = Node(data)

        if self.head is None:
            return False

        current = self.head

        while current.data != node_data and current.next is not None:
            current = current.next

        if current.data != node_data:
            return False

        node.next = current.next
        current.next = node
        self.size += 1

    def add_at_end(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.size += 1
            return
        
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = node
        self.size += 1

    def add_at_index(self, index, data):
        node = Node(data)

        if self.head is None and index != 0:
            return False

        if index == 0:
            node.next = self.head
            self.head = node
            return

        prev = None
        current = self.head
        count = 0

        while current.next and count != index:
            prev = current
            current = current.next
            count += 1

        if count != index:
            return False
        
        prev.next = node
        node.next = current
        self.size += 1

    def print_nodes(self):
        if self.head is None:
            return False

        current = self.head
        nodes = ""

        while current.next is not None:
            nodes += str(current.data) + '-->'
            current = current.next

        nodes + str(current.data)
        print(nodes)