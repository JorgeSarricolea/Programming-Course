# Create a program that asks the user for two matrices of size n x m, where n is the number of rows and m is the number of columns.
# Then, find the matrix product of the two matrices and display it on the screen.

def matrix_product(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    return result

# Ask the user for the size of the matrices
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

# Ask the user for the first matrix
print("Enter the first matrix: ")
matrix1 = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix1.append(row)

# Ask the user for the second matrix
print("Enter the second matrix: ")
matrix2 = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix2.append(row)

# Calculate the matrix product
result = matrix_product(matrix1, matrix2)

# Display the result
print("The matrix product is: ")
for row in result:
    print(row)