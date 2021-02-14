from DataStructures.circular_linked_list import CircularLinkedList

myList = CircularLinkedList()

arr = [12, 43, 17, 91, 103, 2, 0, 57]

for i in arr:
    myList.add(i)

myList.print_nodes()

myList.add_after(55, 2)

myList.print_nodes()

myList.remove(57)

myList.print_nodes()