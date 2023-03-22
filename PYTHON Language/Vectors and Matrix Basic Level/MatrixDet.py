# Create a program that asks the user for a 2x2 matrix. Then, find the determinant of the matrix and display it on the screen.

# Ask the user for the matrix
matrix = input("Enter a 2x2 matrix, separated by spaces and rows by semicolons: ")
matrix = [[float(num) for num in row.split()] for row in matrix.split(";")]

# Calculate the determinant of the matrix
det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

# Print the determinant of the matrix
print("The determinant of the matrix is:", det)
