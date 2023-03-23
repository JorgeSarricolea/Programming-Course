# Create a program that asks the user for a vector of five elements.
# Then, sort the vector from smallest to largest and display the result on the screen.

def sort_vector():
    vector = []
    for i in range(5):
        element = input("Enter an element for the vector: ")
        vector.append(element)

    sorted_vector = sorted(vector)
    print("Sorted vector:", sorted_vector)

sort_vector()