# Create a program that asks the user for a list of numbers and calculates their average. The user must enter the base and height.

# Ask the user for a list of numbers
num_list = input("Enter a list of numbers, separated by spaces: ")

# Convert the input string into a list of floats
num_list = [float(num) for num in num_list.split()]

# Calculate the average of the numbers in the list
avg = sum(num_list) / len(num_list)

# Print the average of the numbers in the list
print("The average of the numbers in the list is:", avg)
