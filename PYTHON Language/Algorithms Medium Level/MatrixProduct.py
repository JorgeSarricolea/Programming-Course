# Create a program that asks the user for two matrices of size n x m, where n is the number of rows and m is the number of columns.
# Then, find the matrix product of the two matrices and display it on the screen.

# Program to find the matrix product of two matrices

# Taking input for the dimensions of the matrices
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

# Taking input for the first matrix
print("Enter the elements of first matrix:")
matrix1 = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix1.append(row)

# Taking input for the second matrix
print("Enter the elements of second matrix:")
matrix2 = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix2.append(row)

# Initializing the product matrix with all zeros
product = [[0 for j in range(m)] for i in range(n)]

# Multiplying the matrices
for i in range(n):
    for j in range(m):
        for k in range(m):
            product[i][j] += matrix1[i][k] * matrix2[k][j]

# Displaying the product matrix
print("Product matrix:")
for row in product:
    print(row)
