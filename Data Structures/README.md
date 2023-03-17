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
