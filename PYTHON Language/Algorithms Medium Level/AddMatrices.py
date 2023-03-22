# Create a program that asks the user for two matrices of equal size.
# Then, find the sum of the two matrices and display it on the screen.

# Ask the user for the matrices
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

print("Enter the values for the first matrix:")
matrix1 = [[float(input()) for j in range(m)] for i in range(n)]

print("Enter the values for the second matrix:")
matrix2 = [[float(input()) for j in range(m)] for i in range(n)]

# Add the two matrices
result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(m)] for i in range(n)]

# Print the resulting matrix
print("The resulting matrix from the addition is:")
for i in range(n):
    for j in range(m):
        print(result_matrix[i][j], end=" ")
    print()
