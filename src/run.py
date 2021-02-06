# from DataStructures.queue import Queue
# from DataStructures.stack import Stack
# from DataStructures.linked_list import LinkedList
from DataStructures.binary_tree import  BinaryTree

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
# my_linked_list = LinkedList()

# for i in range(5):
#     my_linked_list.add(i)

# some_text = "I don't belong here!"

# my_linked_list.add_at_index(3, some_text)

# my_linked_list.print_nodes()

# my_linked_list.remove(some_text)

# my_linked_list.print_nodes()

# my_linked_list.remove_at_index(1)

# my_linked_list.print_nodes()

# Binary Tree
#############################
my_binary_tree = BinaryTree(10)

nums = [12, 18, 3, 5, 19, 7, 5]

for n in nums:
    my_binary_tree.insert(n)

print(my_binary_tree.DFS_in_order())

my_binary_tree.remove(5)

print(my_binary_tree.DFS_in_order())

my_binary_tree.remove(5)

print(my_binary_tree.DFS_in_order())