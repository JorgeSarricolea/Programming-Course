# Write a function that receives an integer and determines whether it is a perfect number or not.
# A number is perfect if it is equal to the sum of its divisors (excluding itself).
# Example: 6 is a perfect number because its divisors are 1, 2, and 3, and 1+2+3=6.

def is_perfect(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    if sum(divisors) == num:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if is_perfect(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")