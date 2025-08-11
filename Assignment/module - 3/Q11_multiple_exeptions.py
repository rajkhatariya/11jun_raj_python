# Q - 11 Write a Python program to demonstrate handling multiple exceptions.

try:
    num1=int(input("enter the value :"))
    num2=int(input("enter the value :"))

    result=num1/num2
    print("Result :",result)

except ValueError:
    print("error! invalid input")

except NameError:
    print("error! try to use a variable that not defined ")
except ZeroDivisionError:
    print("error! not devide by zero")
    