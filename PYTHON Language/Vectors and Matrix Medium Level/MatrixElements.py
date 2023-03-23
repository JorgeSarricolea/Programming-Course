# Create a program that asks the user for a matrix of size n x m and an integer k.
# Then, find the number of elements in the matrix that are greater than k and display it on the screen.

def count_elements(matrix, k):
    count = 0
    for row in matrix:
        for element in row:
            if element > k:
                count += 1
    return count

n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

matrix = []
for i in range(n):
    row = []
    for j in range(m):
        element = int(input(f"Enter the element for row {i+1}, column {j+1}: "))
        row.append(element)
    matrix.append(row)

k = int(input("Enter the value of k: "))

count = count_elements(matrix, k)
print(f"The number of elements in the matrix that are greater than {k} is {count}.")