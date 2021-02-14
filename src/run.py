from DataStructures.circular_linked_list import CircularLinkedList

myList = CircularLinkedList()
print(myList.length())

arr = [12, 43, 17, 91, 103, 2, 0, 57]

for i in arr:
    myList.add(i)

myList.print_nodes()
print(myList.length())
myList.add_after(55, 2)

myList.print_nodes()
print(myList.length())
myList.remove(57)

myList.print_nodes()
print(myList.length())
myList.remove_at_index(1)

myList.print_nodes()
print(myList.length())

for i in arr:
    myList.remove(i)

myList.print_nodes()
print(myList.length())