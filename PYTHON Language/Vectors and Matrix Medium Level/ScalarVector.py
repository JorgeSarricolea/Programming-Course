# Create a program that asks the user for two vectors of equal length.
# Then, find the scalar product of the vectors and display it on the screen.

def scalar_product(v1, v2):
    if len(v1) != len(v2):
        return "Error: Vectors must have the same length."
    else:
        result = 0
        for i in range(len(v1)):
            result += v1[i] * v2[i]
        return result

print("Welcome to Vector Scalar Product Calculator!")
v1 = list(map(int, input("Enter the first vector (separate elements by space): ").split()))
v2 = list(map(int, input("Enter the second vector (separate elements by space): ").split()))

product = scalar_product(v1, v2)

if type(product) == str:
    print(product)
else:
    print("The scalar product of the vectors is:", product)