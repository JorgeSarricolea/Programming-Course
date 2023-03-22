# Create a program that asks the user for two vectors of equal length.
# Then, find the dot product of the vectors and display it on the screen.

# Ask the user for the vectors
n = int(input("Enter the length of the vectors: "))
vector1 = input("Enter the first vector, separated by spaces: ")
vector1 = [float(num) for num in vector1.split()]
vector2 = input("Enter the second vector, separated by spaces: ")
vector2 = [float(num) for num in vector2.split()]

# Find the dot product of the vectors
dot_product = sum([vector1[i]*vector2[i] for i in range(n)])

# Print the dot product of the vectors
print("The dot product of the two vectors is:", dot_product)
