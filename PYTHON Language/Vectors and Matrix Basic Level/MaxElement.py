# Create a program that asks the user for a vector of five elements. Then, find the maximum element in the vector and display its index and corresponding value.

# Ask the user for the vector
vector = input("Enter a vector of five elements, separated by spaces: ")
vector = [float(num) for num in vector.split()]

# Find the index of the maximum element in the vector
max_index = vector.index(max(vector))

# Get the maximum element from the vector
max_element = vector[max_index]

# Print the index and value of the maximum element
print("The maximum element in the vector is at index", max_index, "with a value of", max_element)
