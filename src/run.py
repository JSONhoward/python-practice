from DataStructures.double_linked_list import DoubleLinkedList

myList = DoubleLinkedList()

arr = [12, 43, 17, 91, 103, 2, 0, 57]

for i in arr:
    myList.add(i)

myList.print_nodes()

myList.remove(max(arr))

myList.print_nodes()

myList.remove_at_index(1)

myList.print_nodes()

myList.add_at_tail(7)

myList.print_nodes()