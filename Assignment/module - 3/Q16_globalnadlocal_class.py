# Q - 16  Write a Python program to demonstrate the use of local and global variables in a class.

x=10 #global variable

class localvar:

    def fun(self):
        
        y=15 #local variable

        print("the value of x is :",x)
        print("the vlaue of y is :",y)

ob=localvar()
ob.fun()
