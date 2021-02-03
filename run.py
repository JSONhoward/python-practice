from DataStructures.queue import Queue
from DataStructures.stack import Stack
from DataStructures.linked_list import  Linked_List

# Queue
##############################
# my_queue = Queue()

# for i in range(5):
#     my_queue.enqueue(i)

# my_queue.print_queue()

# stack
#############################
# my_stack = Stack()

# for i in range(5):
#     my_stack.push(i)

# my_stack.print_stack()

# Linked List
#############################
my_linked_list = Linked_List()

for i in range(5):
    my_linked_list.add(i)

my_linked_list.add_at_index(3, "I don't belong here!")

my_linked_list.print_nodes()