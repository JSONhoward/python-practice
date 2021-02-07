class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data

class LinkedList:
    head = None
    size = 0

    def add(self, data):
        '''Add node to list (at head)'''
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
        ''' Add node after another node with passed data'''
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
        '''Add node to end of list (tail)'''
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
        '''Add node at index'''
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

    def remove(self, data):
        '''Remove node that matches passed data'''
        if self.head is None:
            return False
        
        prev = None
        current = self.head

        while current.next is not None and current.data != data:
            prev = current
            current = current.next
        
        if current.data != data:
            return False

        if current.next is not None:
            prev.next = current.next
            current = None
        else:
            prev.next = None
            current = None

    def remove_at_index(self, index):
        '''Remove node from index'''
        if self.head is None:
            return False
        elif index == 0 and self.head.next is not None:
            self.head = self.head.next
            return
        elif index == 0:
            self.head = None
            return
        
        count = 0
        prev = None
        current = self.head

        while current.next is not None and count != index:
            count += 1
            prev = current
            current = current.next
        
        if count != index:
            return False

        prev.next = current.next
        current = None

    def print_nodes(self):
        '''Print all nodes in list'''
        if self.head is None:
            return False

        current = self.head
        nodes = ""

        while current.next is not None:
            nodes += str(current.data) + '-->'
            current = current.next

        nodes + str(current.data)
        print(nodes)