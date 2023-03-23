# Create a program that asks the user for a vector of n elements, where n is an odd number.
#Then, find the middle element of the vector and display it on the screen.

def middle_element_finder():
    n = int(input("Enter the number of elements in the vector (should be odd): "))
    while n % 2 == 0:
        n = int(input("Try again, please enter an odd number: "))

    vector = []
    for i in range(n):
        vector.append(int(input("Enter element {}: ".format(i+1))))

    middle_index = (n-1) // 2
    middle_element = vector[middle_index]

    print("The middle element is: {}".format(middle_element))

if __name__ == '__main__':
    middle_element_finder()
