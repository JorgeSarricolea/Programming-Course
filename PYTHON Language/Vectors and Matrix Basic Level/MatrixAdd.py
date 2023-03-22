# Create a program that asks the user for two 2x2 matrices. Then, print the sum of the matrices.

# Ask the user for the first matrix
matrix1 = input("Enter the first 2x2 matrix, separated by spaces and rows by semicolons: ")
matrix1 = [[float(num) for num in row.split()] for row in matrix1.split(";")]

# Ask the user for the second matrix
matrix2 = input("Enter the second 2x2 matrix, separated by spaces and rows by semicolons: ")
matrix2 = [[float(num) for num in row.split()] for row in matrix2.split(";")]

# Add the matrices element-wise
result = [[matrix1[i][j] + matrix2[i][j] for j in range(2)] for i in range(2)]

# Print the sum of the matrices
print("The sum of the matrices is:")
for row in result:
    print(row)
