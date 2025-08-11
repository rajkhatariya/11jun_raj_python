# Q - 18  Write a Python program to show single inheritance. 
class class1:
    def func(self):
        self.x=10
        self.y=20

class class2(class1):
    def sum(self):
        print("the sum is :",self.x+self.y)

ob=class2()
ob.func()
ob.sum()
