#Task 1: Create functions for each arithmetic operation.

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Divided by 0"
    else:
        return x / y 


#Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

def calculator():

    num1 = int(input("What is your first number: "))
    num2 = int(input("What is your second number? "))
    operation = input("Which operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Can't divide by zero!"
        else:
            result = num1 / num2
    else:
        return "Invalid Operation!"
    return result

print(calculator())