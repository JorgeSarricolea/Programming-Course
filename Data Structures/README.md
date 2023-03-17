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

A stack is a linear data structure that follows the principle of "last in, first out" (LIFO). This means that the last element inserted into the stack is the first one to be removed. This is similar to a stack of plates, where the last plate that was placed on top is the first one to be used.

In terms of implementation, a stack can be built using a list, where adding elements is done with the append() function and removing elements is done with the pop() function without any arguments. Additionally, the peek() function can be used to view the top element of the stack without removing it, and the size() function can be used to get the number of elements in the stack.

```
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


# Example of using the "Stack" data structure.
stack = Stack()

# Check if the stack is empty.
print(stack.is_empty())  # Output: True

# Add elements to the stack.
stack.push(1)
stack.push(2)
stack.push(3)

# Check the size of the stack.
print(stack.size())  # Output: 3

# Check the top element of the stack (without popping it).
print(stack.peek())  # Output: 3

# Pop elements from the stack.
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
print(stack.pop())  # Output: 1

# Check if the stack is empty after popping all elements.
print(stack.is_empty())  # Output: True
```
The above program implements a data structure known as a Stack in Python. A stack is a linear data structure that follows the principle of Last In First Out (LIFO), which means that the last element added to the stack is the first to be removed. The implementation of the stack uses a Python list as its underlying structure.

The constructor of the Stack class initializes an empty list called "items" that will be used to store the elements of the stack. The is_empty() function returns True if the list is empty and False otherwise. The push(item) function adds a new element to the end of the list using the append() method. The pop() function removes the last element added to the list using the pop() method with no arguments, which removes the element at index -1. The size() function returns the length of the list of elements.

## Queues

A queue is a data structure in which elements can be added to the end of the queue and removed from the beginning of the queue. This is known as the First In, First Out (FIFO) principle, which means that the first element to enter the queue is also the first to leave. Queues are commonly used in data processing algorithms and in applications that require real-time event management.

```
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

my_queue = Queue()

# adds the element 5 to the end of the queue
my_queue.enqueue(5)

# adds the element 10 to the end of the queue
my_queue.enqueue(10)

# prints 2
print(my_queue.size())

# removes and returns the first element of the queue (5)
print(my_queue.dequeue())

# prints False, since the queue still has one element (10)
print(my_queue.is_empty())
```

This program defines a Queue class that represents a queue. The queue is implemented as a list of elements called items. The class has four methods:

init(self): the class constructor initializes the items list of elements.
is_empty(self): returns True if the queue is empty, and False otherwise.
enqueue(self, item): adds an element to the queue, at the end of the items list.
dequeue(self): removes and returns the element at the beginning of the queue, i.e., the first element of the items list.
size(self): returns the number of elements in the queue.

## Trees
## Hash tables
