# Create a program that asks the user for a vector of n elements, where n is an odd number.
# Then, find the middle element of the vector and display it on the screen.

# Ask the user for the vector
n = 0
while n % 2 == 0:
    n = int(input("Enter the number of elements in the vector (must be odd): "))
    if n % 2 == 0:
        print("Try again!")

vector = input("Enter the vector, separated by spaces: ")
vector = [float(num) for num in vector.split()]

# Find the middle element of the vector
middle_index = n // 2
middle_element = vector[middle_index]

# Print the middle element of the vector
print("The middle element of the vector is:", middle_element)
