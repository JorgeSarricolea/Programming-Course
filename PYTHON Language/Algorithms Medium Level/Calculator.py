# Create a program that simulates a simple calculator. The program should ask the user to input two numbers
# and an operation (+, -, *, /), and then display the result.

def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: division by zero"

# Main program
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

result = calculator(num1, num2, operation)

print("Result: ", result)