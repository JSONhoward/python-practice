class Node:
    data = None
    prev = None
    next = None

    def __init__(self, data):
        self.data = data

class DoubleLinkedList:
    size = 0

    def __init__(self, head = None):
        self.head = head

    def add(self, data):
        '''Add node'''
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def add_at_tail(self, data):
        '''Add node at tail'''
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            last = None
            current = self.head

            while current is not None:
                last = current
                current = current.next

            last.next = node
            node.prev = last

    def remove(self, data):
        '''Remove node mathing passed in data'''
        if self.head is None:
            return False

        last = None
        current = self.head

        while current.data != data and current.next is not None:
            last = current
            current = current.next

        if current.data != data:
            return False
        
        if current.next is not None:
            last.next = current.next
            current.next.prev = last
        else:
            last.next = None

    def remove_at_index(self, index):
        '''Remove node at index'''
        if self.head is None:
            return False

        count = 0
        last = None
        current = self.head

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        else:
            while count != index and current.next is not None:
                last = current
                current = current.next
                count += 1

            if count != index:
                return False
            
            if current.next is not None:
                last.next = current.next
                current.next.prev = last
            else:
                last.next = None

    def print_nodes(self):
        '''Print all nodes in list'''
        if self.head is None:
            return False

        current = self.head
        nodes = ""

        while current is not None:
            nodes += str(current.data) + ' <--> '
            current = current.next

        print(nodes + 'None')

    def get_head(self):
        return self.head
