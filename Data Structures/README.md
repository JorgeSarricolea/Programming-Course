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

Trees are a hierarchical data structure consisting of nodes interconnected by pointers. Each node has a value and can have zero, one, or two children. Trees are commonly used in data searching and organization.

```
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.add(value, self.root)

    def add(self, value, currentNode):
        if value < currentNode.value:
            if currentNode.left is None:
                currentNode.left = TreeNode(value)
            else:
                self.add(value, currentNode.left)
        elif value > currentNode.value:
            if currentNode.right is None:
                currentNode.right = TreeNode(value)
            else:
                self.add(value, currentNode.right)

    def inorder(self, currentNode):
        if currentNode is not None:
            self.inorden(currentNode.left)
            print(currentNode.valor)
            self.inorden(currentNode.right)

tree = BinaryTree()
tree.add(5)
tree.add(3)
tree.add(7)
tree.add(2)
tree.add(4)
tree.add(6)
tree.add(8)

tree.inorder(tree.root)
```

This program creates a class called NodoArbol that represents a node of a tree, with a value and two pointers, one for the left child and one for the right child. It also creates a class called ArbolBinario that represents the tree itself, with an initially empty root. Then, it defines an agregar() method that adds a new node to the tree in its corresponding position.

The _agregar() method is a helper function that is called recursively to find the appropriate position for the new node, depending on whether its value is greater or less than the value of the current node.

Finally, the program shows the in-order traversal of the tree, which means that all nodes in the left subtree are visited first, then the current node, and then the nodes in the right subtree.

## Hash tables

A hash table is a data structure that uses a hash function to map keys to values. This allows for fast and efficient search of elements in the table through their key. Elements in a hash table can be added, removed, updated, and searched efficiently, making hash tables a very useful data structure in many programming problems.

```
# Creating a hash table
hash_table = {}

# Adding elements to the hash table
hash_table['key1'] = 'value1'
hash_table['key2'] = 'value2'
hash_table['key3'] = 'value3'

# Accessing an element in the hash table
print(hash_table['key2'])  # Output: value2

# Replacing the value of an element in the hash table
hash_table['key3'] = 'new_value'
print(hash_table['key3'])  # Output: new_value

# Removing an element from the hash table
del hash_table['key1']
print(hash_table)  # Output: {'key2': 'value2', 'key3': 'new_value'}

# Checking if a key is in the hash table
if 'key2' in hash_table:
    print("The key 'key2' is in the hash table.")  # Output: The key 'key2' is in the hash table

# Getting a list of all keys in the hash table
keys_list = list(hash_table.keys())
print(keys_list)  # Output: ['key2', 'key3']
```

The above code is an example of working with a hash table in Python.

In the first line, an empty hash table is created using an empty dictionary: hash_table = {}.

Then, three elements are added to the hash table using the key-value format: hash_table['key1'] = 'value1', hash_table['key2'] = 'value2', hash_table['key3'] = 'value3'.

Next, the value associated with the key 'key2' is accessed using the syntax hash_table['key2'], which returns the value 'value2'.

Then, the value of the key 'key3' is replaced with 'new_value' using the syntax hash_table['key3'] = 'new_value', and the new value is printed with print(hash_table['key3']).

Next, the element associated with the key 'key1' is removed using the syntax del hash_table['key1'], and the current hash table is printed with print(hash_table).

It is checked whether the key 'key2' is in the hash table with if 'key2' in hash_table:, and a message is printed if it is true.

Finally, a list of all keys in the hash table is obtained with list(hash_table.keys()), which returns a list of text strings with the values 'key2' and 'key3'.