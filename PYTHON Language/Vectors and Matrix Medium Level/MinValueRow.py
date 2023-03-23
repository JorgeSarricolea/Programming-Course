# Create a program that asks the user for a matrix of size n x m, where n is the number of rows and m is the number of columns.
# Then, find the minimum value of each row and display it on the screen.

def get_matrix(n, m):
    # Create an empty matrix
    matrix = []

    # Get the elements for each row
    for i in range(n):
        row = []
        for j in range(m):
            element = int(input(f"Enter the element for row {i+1} and column {j+1}: "))
            row.append(element)
        matrix.append(row)

    return matrix

def get_min_each_row(matrix):
    min_values = []

    for row in matrix:
        # Find the minimum value for each row
        min_value = min(row)
        min_values.append(min_value)

    return min_values

def main():
    # Ask user for matrix size
    n = int(input("Enter the number of rows: "))
    m = int(input("Enter the number of columns: "))

    # Get the matrix from the user
    matrix = get_matrix(n, m)

    # Find the minimum value of each row
    min_values = get_min_each_row(matrix)

    # Display the result
    print(f"The minimum value of each row is: {min_values}")


if __name__ == "__main__":
    main()