import os
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"
def get_user_input():
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    return num1, operator, num2
while True:
    os.system('cls')
    num1, operator, num2 = get_user_input()
    os.system('cls')
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        print("Invalid operator. Please enter +, -, *, or /.")
        continue
    os.system('cls')
    print("Result: ", result," \n " , " \n ")
    another_calculation = input("Do you want to perform another calculation? (yes(1)/No(0)): ")
    if another_calculation != '1':
        break
