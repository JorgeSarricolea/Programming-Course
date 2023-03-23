# Create a program that asks the user for two matrices of equal size.
# Then, find the sum of the two matrices and display it on the screen.

def add_matrices(mat1, mat2):
    """Add two matrices element-wise"""
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result

def read_matrix():
    """Read a matrix from user input"""
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"Enter the value for ({i}, {j}): "))
            row.append(val)
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    """Display a matrix on the screen"""
    for row in matrix:
        print(row)

def main():
    """Main function to add matrices"""
    print("Enter the first matrix:")
    matrix1 = read_matrix()
    print("Enter the second matrix:")
    matrix2 = read_matrix()
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Error: matrices must be of equal size")
        return
    result = add_matrices(matrix1, matrix2)
    print("The sum of the matrices is:")
    display_matrix(result)

if __name__ == "__main__":
    main()