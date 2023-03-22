# Create a program that asks the user for a matrix of size n x m, where n is the number of rows and m is the number of columns.
# Then, find the minimum value of each row and display it on the screen.

# Ask for matrix dimensions
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

# Initialize matrix with zeros
matrix = [[0 for j in range(m)] for i in range(n)]

# Ask for matrix elements
for i in range(n):
    for j in range(m):
        matrix[i][j] = int(input(f"Enter element {i+1},{j+1}: "))

# Find minimum of each row
min_each_row = []
for row in matrix:
    min_val = row[0]
    for val in row:
        if val < min_val:
            min_val = val
    min_each_row.append(min_val)

# Display results
print("Minimum value of each row:")
for i, val in enumerate(min_each_row):
    print(f"Row {i+1}: {val}")
