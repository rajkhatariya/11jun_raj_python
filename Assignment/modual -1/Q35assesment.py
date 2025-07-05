# q - 35  Create a mini-project where students combine conditional statements, loops, and functions 
#to create a basic Python application, such as a simple calculator or a grade management system


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"

while True:
    print("\n==============================")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an operation (1-5): ")

    if choice == '5':
        print("Exiting the calculator")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("The additon is :", add(num1, num2))
    elif choice == '2':
        print("The subtraction is :", subtract(num1, num2))
    elif choice == '3':
        print("The multiplication is :", multiply(num1, num2))
    elif choice == '4':
        print("The divition is :", divide(num1, num2))
    else:
        print("Invalid choice")
