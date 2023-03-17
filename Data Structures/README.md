# Data structures

Data structures are a way of organizing and storing data on a computer so that it can be efficiently used. Imagine you have a box with a bunch of objects inside, and you need to find a particular object. If the box isn't organized in some way, you'll have to go through each object one by one until you find the one you need. But if the objects are organized into compartments or drawers, you can find the object much faster and more efficiently.

In programming, data structures are very similar. There are different types of data structures used to store different types of data, and each structure has its own advantages and disadvantages in terms of efficiency and ease of use. For example, some types of data structures are better for quickly searching for specific data, while others are better for adding or removing data.

Some common examples of data structures include:

- Arrays
- Linked lists
- Stacks
- Queues
- Trees
- Hash tables

As you learn more about programming and software development, you'll learn how to use these data structures to solve problems and improve the efficiency of your programs.

Below you will find an example of each type of data structure, programmed in Python:


## Arrays

An array is a data structure that stores a collection of elements, typically of the same data type, in a contiguous block of memory. Each element in the array is identified by its index, which is an integer value representing its position in the array. Arrays are commonly used in programming to store and manipulate data efficiently, as they allow for direct access to any element in constant time. They can be initialized with a fixed size or dynamically resized as needed.

```
# Create an array of integers.
arr = [1, 2, 3, 4, 5]

# Print the complete array.
print("Array:", arr)

# Access the first element of the array. (index 0)
print("The first element is:", arr[0])

# Access the last element of the array. (index -1)
print("The last element is:", arr[-1])

# Modify an element of the array. (index 3)
arr[3] = 10
print("The new element is", arr)

# Get the length of the array.
print("The length of the array is:", len(arr))

# Iterate over the array using a for loop.
print("The elements of the array are:")
for element in arr:
    print(element)
```

In this program, an array of integers called "arr" is created using brackets and separating the elements with commas. Then, the complete array is printed using the "print" function.

The elements of the array are accessed using indices, where the first element has index 0 and the last has index -1. To modify an element, simply assign a new value to the corresponding index.

The length of the array is obtained using the "len" function. To traverse the array, a for loop is used, where each element is assigned to the variable "element" in each iteration of the loop.

## Linked lists

A linked list is a data structure that consists of a sequence of elements, where each element contains a reference to the next element in the sequence. Unlike arrays, linked lists do not have a fixed size and can easily grow or shrink as needed. Each element in a linked list is called a node, and contains two parts: data and a reference to the next node in the list. The first node in the list is called the head, while the last node in the list points to null. Linked lists can be used to implement various data structures such as stacks, queues, and associative arrays.

```
# Definition of the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Definition of the Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Function to print the linked list.
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

# Example of using linked list.
llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
llist.head.next = second
second.next = third
llist.printList()
```

This program defines a Node class that represents the nodes that make up the linked list. Each node has a value (data) and a pointer to the next node (next).

Then, the LinkedList class is defined, which represents the linked list itself. It has a head attribute that represents the first node of the list.

The printList function traverses the linked list and prints the values of each node.

Finally, an example of using the linked list is created. An instance of the LinkedList class is created and three nodes are added to the list, whose values are 1, 2, and 3. Then, the linked list is printed using the printList function.

## Stacks
## Queues
## Trees
## Hash tables
