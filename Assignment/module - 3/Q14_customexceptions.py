# Q - 14  Write a Python program to print custom exceptions. 

class NegativeNumberError(Exception):
    pass  

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Error: Negative number entered.")
    print(f"You entered: {num}")

except NegativeNumberError as e:
    print(e)

except ValueError:
    print("Error: Please enter a valid integer.")

finally:
    print("Program execution finished.")
