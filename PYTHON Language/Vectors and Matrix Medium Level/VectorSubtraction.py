# Create a program that asks the user for two vectors of equal length.
# Then, find the resulting vector from the subtraction of the two vectors and display it on the screen.

def vector_subtraction(vector1, vector2):
    """
    Subtracts two vectors element-wise and returns the resulting vector.
    """
    result = []
    for i in range(len(vector1)):
        result.append(vector1[i] - vector2[i])
    return result

# Ask the user for two vectors of equal length
vector1 = input("Enter the first vector (comma-separated): ").split(',')
vector2 = input("Enter the second vector (comma-separated): ").split(',')

# Convert the input strings to lists of integers
vector1 = [int(x) for x in vector1]
vector2 = [int(x) for x in vector2]

# Check that the vectors have equal length
if len(vector1) != len(vector2):
    print("Error: the vectors must have equal length.")
else:
    # Calculate the resulting vector from the subtraction of the two vectors
    result = vector_subtraction(vector1, vector2)
    # Display the resulting vector
    print("The resulting vector is:", result)