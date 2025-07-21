# Q - 23 • Write a Python program to create a calculator using functions. 
a= float(input("enter the value :"))
b=float(input("enter the value :"))

def add():
    print("the addition is :",a+b)
def sub():
    print("the subtraction is :",a-b)
def mul():
    print("the multiplication is :",a*b)
def div():
    print("the divition is :",a/b)

print("press 1 for addition")
print("press 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for divition")
print("===================================")

n=int(input("enter your choise :"))

if n==1:
    add()
elif n==2:
    sub()
elif n==3:
    mul()
elif n==4:
    div()
else:
    print("wronge choise ")


    