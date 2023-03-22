# Create a program that asks the user for two vectors of equal length.
# Then, find the resulting vector from the subtraction of the two vectors and display it on the screen.

# Ask the user for the vectors
n = int(input("Enter the length of the vectors: "))
vector1 = input("Enter the first vector, separated by spaces: ")
vector1 = [float(num) for num in vector1.split()]
vector2 = input("Enter the second vector, separated by spaces: ")
vector2 = [float(num) for num in vector2.split()]

# Subtract the second vector from the first vector
result_vector = [vector1[i]-vector2[i] for i in range(n)]

# Print the resulting vector
print("The resulting vector from the subtraction is:", result_vector)
