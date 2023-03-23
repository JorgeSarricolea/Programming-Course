# Write a program with a function that receives a list of integers and returns the sum of the even numbers in the list.

def sum_even(lst):
    """
    Returns the sum of the even numbers in the list
    """
    return sum(filter(lambda x: x % 2 == 0, lst))

if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"The sum of even numbers in the list {lst} is {sum_even(lst)}")