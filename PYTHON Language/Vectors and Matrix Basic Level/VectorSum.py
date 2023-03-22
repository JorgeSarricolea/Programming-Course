# Create a program that asks the user for two vectors of three elements each. Then, print the sum of the vectors.

# Ask the user for the first vector
vector1 = input("Enter the first vector, separated by spaces: ")
vector1 = [float(num) for num in vector1.split()]

# Ask the user for the second vector
vector2 = input("Enter the second vector, separated by spaces: ")
vector2 = [float(num) for num in vector2.split()]

# Calculate the sum of the two vectors
sum_vector = [vector1[i] + vector2[i] for i in range(3)]

# Print the sum of the two vectors
print("The sum of the two vectors is:", sum_vector)
