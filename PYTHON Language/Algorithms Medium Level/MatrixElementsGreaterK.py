# Create a program that asks the user for a matrix of size n x m and an integer k.
# Then, find the number of elements in the matrix that are greater than k and display it on the screen.

# matrix_elements_greater_than_k.py

n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

matrix = []

for i in range(n):
    row = []
    for j in range(m):
        element = int(input("Enter an element: "))
        row.append(element)
    matrix.append(row)

k = int(input("Enter a value for k: "))

count = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] > k:
            count += 1

print(f"The number of elements greater than {k} in the matrix is {count}.")
