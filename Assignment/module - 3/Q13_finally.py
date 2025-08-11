# Q - 13  Write a Python program to handle file exceptions and use the finally block for closing the file.

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2
    print("Result :",result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter numeric values only.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("Execution of the program is complete.")
