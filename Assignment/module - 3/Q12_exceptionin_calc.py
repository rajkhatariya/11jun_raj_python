# Q - 12     Write a Python program to handle exceptions in a calculator
def calculator():
    try:
        n1=float(input("enter the value :"))
        n2=float(input("enter the value :"))
        op=input("enter the operation (+,-,*,/) :")

        if op=='+':
            print("the addition is :",n1+n2)
        elif op=='-':
            print("the subtraction is :",n1-n2)
        elif op=='*':
            print("the multiplacation is :",n1*n2)
        elif op=='/':
            print("the divition is :",n1/n2)
        else:
            print("invalid input!")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except ValueError:
        print("Error: Please enter valid numeric values.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

calculator()