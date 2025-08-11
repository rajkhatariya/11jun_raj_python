# Q - 10 Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input). 

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = num1 / num2
    print(f"The result of {num1} / {num2} is: {result}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

