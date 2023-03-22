# Create a program that asks the user for a vector of five elements.
# Then, sort the vector from smallest to largest and display the result on the screen.

# Ask the user for the vector
vector = input("Enter the vector, separated by spaces: ")
vector = [float(num) for num in vector.split()]

# Sort the vector from smallest to largest
sorted_vector = sorted(vector)

# Print the sorted vector
print("The sorted vector is:", sorted_vector)
